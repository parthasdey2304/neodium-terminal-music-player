#!/bin/bash

# Check if Python 3, pip, and python-is-python3 are already installed
if command -v python3 &>/dev/null && command -v pip3 &>/dev/null && command -v python-is-python3 &>/dev/null; then
    echo "Python 3, pip, and python-is-python3 are already installed."
else
    # Check if running as root
    if [ "$EUID" -ne 0 ]; then
        echo "Please run this script as root or using sudo."
        exit 1
    fi

    # Detect package manager and install Python 3, pip, and python-is-python3
    if command -v apt &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using apt..."
        apt update
        apt install -y python3 python3-pip python-is-python3
    elif command -v pacman &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using pacman..."
        pacman -Sy --noconfirm python python-pip
        pacman -S --noconfirm python-is-python3
    elif command -v dnf &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using dnf..."
        dnf install -y python3 python3-pip python3-is-python3
    elif command -v yum &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using yum..."
        yum install -y python3 python3-pip python-is-python3
    else
        echo "Unsupported package manager. Please install Python 3, pip, and python-is-python3 manually."
        exit 1
    fi

    # Check if Python 3, pip, and python-is-python3 installation was successful
    if ! command -v python3 &>/dev/null || ! command -v pip3 &>/dev/null || ! command -v python-is-python3 &>/dev/null; then
        echo "Failed to install Python 3, pip, and python-is-python3."
        exit 1
    fi
fi

# Install necessary Python packages using pip
echo "Installing Python packages using pip..."
pip3 install --upgrade pip
pip3 install playsound google-api-python-client pytube

echo "Setup completed successfully."
exit 0
