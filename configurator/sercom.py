import time

import serial
import os
import serial.tools.list_ports


def get_port():
    """Returns the port of the device"""
    env = os.environ.get('SERIAL_PORT')
    if env:
        return env
    else:
        ports = serial.tools.list_ports.comports()
        if len(ports) == 0:
            raise Exception("No serial port found")
        elif len(ports) > 1:
            print("W> Multiple serial ports found:")
            for port in ports:
                print("W> " + port.device)
            return input("W> Please enter the port of the device: ")
        else:
            print("I> Found serial port: " + ports[0].device)
            return ports[0].device


class SerialSwarm:
    def __init__(self):
        self.ser = serial.Serial(get_port(), 115200, timeout=5)
        self.ser.flush()

    def send(self, cmd):
        """Sends a command to the device"""
        self.ser.write(cmd.encode("UTF-8") + b"\r\n")
        self.ser.flush()
        time.sleep(0.5)

    def wait_boot(self):
        """Waits for a response from the device"""
        kelda = False
        while True:
            message = self.ser.readline()
            try:
                print(message.decode("UTF-8"), end="")
            except UnicodeDecodeError:
                print(message, end="")
            if b"KELDA" in message:
                kelda = True
            if message.startswith(b"Boot "):
                time.sleep(3)

                # read the rest of the boot message
                while self.ser.in_waiting > 0:
                    x = self.ser.read(1)
                    try:
                        print(x.decode("UTF-8"), end="")
                    except UnicodeDecodeError:
                        print(x, end="")
                return message.decode("UTF-8").removesuffix("\n").removesuffix("\r"), kelda

    def boot(self):
        """Returns the device's name"""
        b, iskelda = self.wait_boot()
        host, serialnr_complex = b.removeprefix("Boot ").split(" ")

        serialnr = serialnr_complex.split(":")[1].split(")")[0]

        return host, "ftSwarm" + serialnr, iskelda

    def to_the_setup(self, kelda):
        """Sends the command to go to the setup menu"""
        if kelda:
            self.send("setup")

    def configure_ledcount(self, kelda, ledcount):
        """Configures the number of LEDs"""
        self.to_the_setup(kelda)
        self.send("1")
        self.send("5")
        self.send(str(ledcount))
        self.send("0")
        self.send("Y")
        self.wait_boot()

    def into_aliases(self, kelda):
        """Sends the command to go to the alias menu"""
        self.to_the_setup(kelda)
        self.send("3")

    def set_alias(self, nr, value):
        """Sets an alias"""
        self.send(str(nr))
        self.send(value)

    def save_aliases(self):
        """Saves the aliases"""
        self.send("0")
        self.send("Y")

    def done(self):
        """Closes the serial connection"""
        self.send("0")
        self.wait_boot()
        self.ser.close()

