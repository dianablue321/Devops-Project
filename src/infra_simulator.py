import subprocess
from src.input_handler import collect_input
from src.machine import Machine
import logging
import os

os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    filename="../logs/provisioning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_bash_script(script_path):
    try:
        result = subprocess.run(["bash", script_path], check=True, capture_output=True, text=True)
        logging.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running script {script_path}: {e.stderr}")

def main():
    logging.info("Provisioning started.")
    
    machines_data = collect_input()
    machines = [Machine(**data) for data in machines_data]

    for machine in machines:
        logging.info(f"Configuring services for {machine.name}")
        run_bash_script("../scripts/install_nginx.sh")
    
    logging.info("Provisioning completed.")

if __name__ == "__main__":
    main()
