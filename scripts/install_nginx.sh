#!/bin/bash
LOG_FILE="../logs/provisioning.log"

echo "Starting Nginx installation..." | tee -a $LOG_FILE

if ! command -v nginx &> /dev/null; then
    if [ -x "$(command -v apt)" ]; then
        sudo apt update && sudo apt install -y nginx
    elif [ -x "$(command -v yum)" ]; then
        sudo yum install -y nginx
    else
        echo "Unsupported OS. Manual installation needed." | tee -a $LOG_FILE
        exit 1
    fi
    if [ $? -eq 0 ]; then
        echo "Nginx installed successfully." | tee -a $LOG_FILE
    else
        echo "Error installing Nginx." | tee -a $LOG_FILE
        exit 1
    fi
else
    echo "Nginx is already installed." | tee -a $LOG_FILE
fi
