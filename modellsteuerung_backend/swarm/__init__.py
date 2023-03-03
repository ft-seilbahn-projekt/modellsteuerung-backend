from threading import Thread
from time import sleep

from ..logger import get_logger


class SwarmBackend(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.teardown_requested = False
        self.logger = get_logger(__name__)

    def run(self):
        while not self.teardown_requested:
            self.logger.info("Swarm Backend is running")
            sleep(1)

        self.logger.debug("Swarm Backend is shutting down")


backend = SwarmBackend()
