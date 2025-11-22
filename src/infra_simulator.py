import json
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from machine import Machine
from logger_setup import get_logger
import subprocess

logger = get_logger("infra")

CONFIG_FILE = Path("../configs/instances.json")
CONFIG_FILE.parent.mkdir(exist_ok=True)

# Pydantic model for input validation
class MachineInput(BaseModel):
    name: str = Field(..., min_length=1)
    os: str
    cpu: int = Field(..., ge=1, le=32)
    ram: int = Field(..., ge=1, le=128)

def prompt_user():
    name = input("VM Name: ")
    os = input("OS (ubuntu/debian/centos): ")
    cpu = int(input("CPU cores: "))
    ram = int(input("RAM (GB): "))

    try:
        validated = MachineInput(name=name, os=os, cpu=cpu, ram=ram)
        machine = Machine(**validated.dict())
        save_machine(machine)
        logger.info(f"Machine '{name}' saved successfully.")
    except ValidationError as e:
        logger.error(f"Validation error: {e}")

def save_machine(machine: Machine):
    if CONFIG_FILE.exists():
        data = json.loads(CONFIG_FILE.read_text())
    else:
        data = {"instances": []}

    data["instances"].append(machine.to_dict())
    CONFIG_FILE.write_text(json.dumps(data, indent=4))

def run_setup_script(machine: Machine):
    try:
        subprocess.run(["bash", "../scripts/install_nginx.sh"], check=True)
        logger.info(f"Services installed on {machine.name}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Service installation failed: {e}")
