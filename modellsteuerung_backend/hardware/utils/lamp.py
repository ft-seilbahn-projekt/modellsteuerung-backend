import asyncio

from swarm import FtSwarmLamp


class BlinkingLamp:
    def __init__(self, lamp: FtSwarmLamp, speed=0.5):
        self.speed = speed
        self.lamp = lamp
        self.on = False
        self.blinking = False
        self.disabled = True

        asyncio.create_task(self.scheduler())

    async def scheduler(self):
        while True:
            if self.blinking and not self.disabled:
                if self.on:
                    await self.lamp.on()
                else:
                    await self.lamp.off()
                self.on = not self.on
            await asyncio.sleep(self.speed)

    async def on(self):
        if self.on:
            return
        self.disabled = True
        self.blinking = False
        self.on = True
        await self.lamp.on()

    async def off(self):
        if not self.on:
            return
        self.disabled = True
        self.blinking = False
        self.on = False
        await self.lamp.off()

    async def blink(self):
        if self.blinking:
            return
        self.disabled = False
        self.blinking = True
        self.on = True
        await self.lamp.on()

