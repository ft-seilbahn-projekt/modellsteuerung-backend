import time

from swarm import FtSwarm, FtSwarmAnalogInput

from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.utils import PersistedFiFo

NTCS = {
    "spbntc": "Talstation/Spinelli hinten"
}


class NtcSense(Modifier):
    _ntcs: dict[str, FtSwarmAnalogInput] = {}
    _ntc_queue = {}

    _last_time_measurement = 0

    async def register(self, swarm: FtSwarm):
        self.logger.info("Registering NTCs")
        for sensor in NTCS:
            # noinspection PyProtectedMember
            self._ntcs[sensor] = await swarm._get_object(sensor, FtSwarmAnalogInput, True, 1)
            self._ntc_queue[sensor] = PersistedFiFo(10, "ntc_" + sensor)

    async def process(self):
        if self._last_time_measurement + 60 > time.time():
            return

        self.logger.info("Measuring NTCs")
        all_measurements = []
        for sensor, hw in self._ntcs.items():
            x = await hw.get_value()
            self._ntc_queue[sensor].append(f"{time.time()}:{x}")
            all_measurements.append(x)

        normal_temperature = sum(all_measurements) / len(all_measurements)
        self.logger.info(f"Normal temperature: {normal_temperature}")

        self._last_time_measurement = time.time()

    def get_ids(self) -> list[str]:
        return list(NTCS.keys())

    def get_data(self, sensor_id: str) -> list[str]:
        return self._ntc_queue[sensor_id].get_all()

    def get_name(self, sensor_id: str) -> str:
        return NTCS[sensor_id]


ntc = NtcSense()
