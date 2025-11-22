from logger_setup import get_logger

logger = get_logger("machine")

class Machine:
    def __init__(self, name: str, os: str, cpu: int, ram: int):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        logger.info(f"Machine created: {self.name}, OS: {self.os}, CPU: {self.cpu}, RAM: {self.ram}GB")

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }
