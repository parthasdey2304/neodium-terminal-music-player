#!/bin/bash

# Check if Python 3, pip, and python-is-python3 are already installed
if command -v python3 &>/dev/null && command -v pip3 &>/dev/null && command -v python-is-python3 &>/dev/null; then
    echo "Python 3, pip, and python-is-python3 are already installed."
else
    # Detect package manager and install Python 3, pip, and python-is-python3
    if command -v apt &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using apt..."
        sudo apt update
        sudo apt install -y python3 python3-pip python-is-python3
    elif command -v pacman &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using pacman..."
        sudo pacman -Sy --noconfirm python python-pip
        sudo pacman -S --noconfirm python-is-python3
    elif command -v dnf &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using dnf..."
        sudo dnf install -y python3 python3-pip python3-is-python3
    elif command -v yum &>/dev/null; then
        echo "Installing Python 3, pip, and python-is-python3 using yum..."
        sudo yum install -y python3 python3-pip python-is-python3
    else
        echo "Unsupported package manager. Please install Python 3, pip, and python-is-python3 manually."
        exit 1
    fi
fi

# Install necessary Python packages using pip
echo "Installing Python packages using pip..."
pip install --upgrade pip
pip install playsound google-api-python-client pytube

# Copyin the neodium bash and python script to /bin
sudo cp neodium /bin/
sudo cp neodium.py /bin/

# Making the neodium bash script executable
sudo chmod +x /bin/neodium
sudo chmod +x /bin/neodium.py

echo "Setup completed successfully."
exit 0