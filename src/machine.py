import logging
import os

os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    filename="../logs/provisioning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        logging.info(f"Machine created: {self.name} ({self.os}, {self.cpu} CPU, {self.ram}GB RAM)")

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }
