import json

from configurator.sercom import SerialSwarm
from configurator.swarm_types import TYPES
import sys
import os


def compute_id(sw_type, port: str):
    a = TYPES[sw_type]["a"]
    m = TYPES[sw_type]["m"]
    if port == "hostname":
        return 1

    if port.startswith("A"):
        return int(port[1:]) + 1
    elif port.startswith("M"):
        return int(port[1:]) + 1 + a
    elif port.startswith("LED"):
        return int(port[3:]) + 1 + a + m
    else:
        raise ValueError("Invalid port: " + port)


def main():
    # pick name from cli args
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print("L> Configuring as: " + name)
    else:
        print("E> No name provided. Aborting.")
        return

    sw = SerialSwarm()
    print("L> Awaiting Boot...")
    host, sername, iskelda = sw.boot()
    print("L> Hostname: " + host)
    print("L> Serial Name: " + sername)
    print("L> Is Kelda: " + str(iskelda))

    # look for a file in configurations/{name}/*.json that contains a name in "names"
    filepath = None
    for file in os.listdir("configurations/" + name):
        if not file.endswith(".json"):
            continue
        with open("configurations/" + name + "/" + file, "r") as f:
            config = json.load(f)
            if sername in config["names"]:
                filepath = "configurations/" + name + "/" + file
                break

    if filepath is None:
        print("E> No configuration found for " + sername + ". Aborting.")
        return

    print("L> Loading configuration from " + filepath)
    with open(filepath, "r") as f:
        config = json.load(f)

    # configure the number of LEDs
    print("L> Configuring LED count to " + str(config["maxled"]))
    sw.configure_ledcount(iskelda, config["maxled"])
    sw.into_aliases(iskelda)
    for io in config["io"]:
        print("L> Set alias for " + io["id"] + " to " + io["value"])
        sw.set_alias(compute_id(config["type"], io["id"]), io["value"])

    sw.save_aliases()
    print("L> Done!")
    sw.done()
    print("L> Exiting...")


if __name__ == '__main__':
    main()
