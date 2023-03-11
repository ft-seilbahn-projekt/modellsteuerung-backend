from modellsteuerung_backend.utils import Level


class InboundDriveCtlPacket:
    """
    A packet for the DriveCtl protocol.
    """

    def __init__(self, raw_data: bytes):
        self.raw_data = raw_data
        self._speed = None
        self._error = None
        self._parse()

    def _parse(self):
        """
        Parses the raw data in the following format

        a a a a a a a a b b b b b b b b
        a = number that corresponds to a warning level (NotificationLevel)
        b = speed * 10

        :return: None
        """

        if len(self.raw_data) != 2:
            return

        try:
            self._error = self.raw_data[0]
            self._speed = self.raw_data[1] / 10
        except ValueError:
            pass

    def get_speed(self):
        return self._speed

    def get_error(self):
        if self._error == 0:
            return Level.INFO
        elif self._error == 1:
            return Level.WARNING
        elif self._error == 2:
            return Level.FATAL
