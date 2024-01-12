import datetime

from swarm import FtSwarm

from modellsteuerung_backend.hardware.io import Input
from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.hardware.utils.LEDGroup import LEDGroup, get_led_group
from modellsteuerung_backend.hardware.utils.flank import FlankedSwitch


class LEDs(Modifier):
    _in_onoff: FlankedSwitch  # enable for LEDs

    # only with on
    _grp_transport: LEDGroup
    _grp_tracks: LEDGroup

    # with on or night
    _grp_flight: LEDGroup
    _grp_top: LEDGroup

    def __init__(self):
        super().__init__()

        self.force_on = False
        self.on = False

        self._should_be_on_night = False
        self._should_be_on = False

    async def register(self, swarm: FtSwarm):
        self._in_onoff = FlankedSwitch(await swarm.get_switch(Input.DESK_ON_OFF))
        # TODO add real LEDs
        self._grp_transport = await get_led_group(swarm, [], 0, "osimf", 0xffffff)
        self._grp_tracks = await get_led_group(swarm, [], 0, "osimb", 0xffffff)
        # ICAO type e
        self._grp_flight = await get_led_group(swarm, [], 1.5, "osimfl", 0xff0000)
        self._grp_top = await get_led_group(swarm, [], 0, "osimn", 0xff0000)

        await self._grp_top.off()
        await self._grp_flight.off()
        await self._grp_tracks.off()
        await self._grp_transport.off()

    async def process(self):
        # check if before 6 or after 19
        now = datetime.datetime.now()
        if now.hour < 6 or now.hour >= 19:
            self.force_on = True
        else:
            self.force_on = False

        if await self._in_onoff.get_flank():
            self.on = not self.on

        night_on = self.force_on or self.on

        if night_on != self._should_be_on_night:
            self._should_be_on_night = night_on
            if night_on:
                await self._grp_flight.on()
                await self._grp_top.on()
            else:
                await self._grp_flight.off()
                await self._grp_top.off()

        if self.on != self._should_be_on:
            self._should_be_on = self.on
            if self.on:
                await self._grp_transport.on()
                await self._grp_tracks.on()
                await self._grp_flight.on()
                await self._grp_top.on()
            else:
                await self._grp_transport.off()
                await self._grp_tracks.off()
                await self._grp_flight.off()
                await self._grp_top.off()
                self._should_be_on_night = False


leds = LEDs()
