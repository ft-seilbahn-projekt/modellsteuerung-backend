import asyncio

from swarm import FtSwarm, FtSwarmLamp, FtSwarmPixel
from abc import ABC, abstractmethod

from modellsteuerung_backend.utils import is_emulated


class LED(ABC):
    @abstractmethod
    async def register(self):
        pass

    @abstractmethod
    async def on(self):
        pass

    @abstractmethod
    async def off(self):
        pass


class LampLEDImpl(LED):
    def __init__(self, led: FtSwarmLamp):
        self.led = led

    async def register(self):
        pass

    async def on(self):
        await self.led.on()

    async def off(self):
        await self.led.off()


class ColorLEDImpl(LED):
    def __init__(self, led: FtSwarmPixel, color: int):
        self.led = led
        self.color = color

    async def register(self):
        await self.led.set_brightness(100)

    async def on(self):
        await self.led.set_color(self.color)

    async def off(self):
        await self.led.set_color(0)


class LEDGroup:
    def __init__(self, leds: list[str], blink: float = 0, emulated_led: str = None, emulated_color: int = None):
        self.leds = leds
        self.emulated_led = emulated_led
        self.emulated_color = emulated_color
        self.blink = blink

        self._leds: list[LED] = []
        self._on = False

    async def register(self, swarm: FtSwarm):
        if is_emulated() and self.emulated_led:
            if self.emulated_color:
                self._leds = [ColorLEDImpl(await swarm.get_pixel(self.emulated_led), self.emulated_color)]
            else:
                self._leds = [LampLEDImpl(await swarm.get_lamp(self.emulated_led))]
        else:
            self._leds = [await swarm.get_lamp(led) for led in self.leds]

        for led in self._leds:
            await led.register()

        if self.blink > 0:
            # noinspection PyAsyncCall
            asyncio.create_task(self.blink_loop())

    async def on(self):
        self._on = True
        for led in self._leds:
            await led.on()

    async def blink_loop(self):
        if self.blink == 0:
            return
        while True:
            if not self._on:
                await asyncio.sleep(0.1)
                continue
            for led in self._leds:
                await led.on()
            await asyncio.sleep(self.blink)
            for led in self._leds:
                await led.off()
            await asyncio.sleep(self.blink)

    async def off(self):
        self._on = False
        for led in self._leds:
            await led.off()


async def get_led_group(swarm: FtSwarm, leds: list[str], blink=0, emulated_led: str = None, emulated_color: int = None):
    led_group = LEDGroup(leds, blink, emulated_led, emulated_color)
    await led_group.register(swarm)
    return led_group
