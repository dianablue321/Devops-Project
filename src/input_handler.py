from pydantic import BaseModel, validator
from typing import List
import json
import os

CONFIG_FILE = "../configs/instances.json"

class MachineModel(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int  # in GB

    @validator("os")
    def os_must_be_valid(cls, v):
        valid_os = ["ubuntu", "centos", "debian"]
        if v.lower() not in valid_os:
            raise ValueError(f"OS must be one of {valid_os}")
        return v.lower()

    @validator("cpu", "ram")
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Value must be positive")
        return v

def collect_input() -> List[dict]:
    machines = []
    while True:
        try:
            name = input("Enter machine name: ")
            os_name = input("Enter OS (ubuntu/centos/debian): ")
            cpu = int(input("Enter CPU cores: "))
            ram = int(input("Enter RAM (GB): "))
            machine = MachineModel(name=name, os=os_name, cpu=cpu, ram=ram)
            machines.append(machine.dict())
        except Exception as e:
            print(f"Error: {e}")
            continue
        cont = input("Add another machine? (y/n): ").lower()
        if cont != 'y':
            break
    # Save to JSON
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(machines, f, indent=4)
    return machines
