import asyncio
import json


class MockFtSwarmSwitch:
    def __init__(self, swarm, name) -> None:
        self.swarm = swarm
        self.name = name
        self.state = False
        self.events = []
        self.flank_state = False

    async def wait(self):
        ev = asyncio.Event()
        self.events.append(ev)
        await ev.wait()
        self.events.remove(ev)

    async def handle_input(self, inp):
        self.state = False if inp == 0 else True
        for event in self.events:
            event.set()

    def get_flank(self):
        """
        Returns the flank of the switch
        """
        if self.flank_state != self.state:
            self.flank_state = self.state
            return self.state
        return False

    async def postinit(self):
        pass


MOCK_CLASSES = {
    "digital": MockFtSwarmSwitch
}


class Mocks:
    def __init__(self):
        self.data = {}
        self.loaded_mocks = {}
        self.mock_instances = {}

    async def update(self):
        with open("mocks.json", "r") as f:
            self.data = json.load(f)

        mocked_sets = self.data["mocked_sets"]
        for object_key in self.data["objects"].keys():
            obj = self.data["objects"][object_key]
            sets = obj["sets"]
            is_mocked = False
            for set_key in sets:
                if set_key in mocked_sets:
                    is_mocked = True
                    break

            if not is_mocked:
                continue

            # Add to loaded mocks
            self.loaded_mocks[object_key] = self.data["objects"][object_key]

        # Update all current instances
        for name in self.mock_instances.keys():
            if name not in self.loaded_mocks.keys():
                continue

            instance = self.mock_instances[name]
            await instance.handle_input(self.loaded_mocks[name]["value"])

    async def is_mocked(self, name):
        await self.update()
        return name in self.loaded_mocks.keys()

    def get_mock_class(self, name):
        return MOCK_CLASSES[self.loaded_mocks[name]["type"]]

    def register_mock(self, name, instance):
        self.mock_instances[name] = instance
