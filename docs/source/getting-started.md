# Getting Started

In this guide, you will learn how to install and use JNote.

## Requirements

In order to work properly, JNote requires at least the following specifications:

* Windows(32 or 64 bit), Mac or Linux operating system(OS).
* 4 GB RAM.
* 50 ~ 240 MB storage (Depends on the operationg system).

## Installation

Follow the below steps to install JNote according to your OS.

### Windows and Mac

1. Download the corresponding `.zip` file for your platform [here](https://github.com/Dev-I-J/JNote/releases/latest):
    * `JNote-Windows-32.zip` - JNote For Windows 32 bit.
    * `JNote-Windows-64.zip` - JNote For Windows 64 bit.
    * `JNote-Mac.zip` - JNote For Mac.

2. Extract the `zip` where you would link to have JNote installed.

3. Run JNote
    * Mac - Double click `JNote.app`
    * Windows - Go to the JNote folder and double click `JNote.exe`

### Linux

#### Steps

1. Clone JNote:
    ```bash
    sudo apt-get update
    sudo apt-get install git
    git clone https://github.com/Dev-I-J/JNote.git
    cd JNote
    ```

2. Install `python`:
    ```bash
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.9
    ```

3. Install `pip`:
    ```bash
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    ```

4. Setup Virtualenv:
    ```bash
    python3 -m pip install virtualenv
    python3 -m virtualenv buildenv
    source buildenv/bin/activate
    ```

5. Install Dependencies:
    ```bash
    python3 -m pip install PyInstaller
    python3 -m pip install -r requirements.txt
    ```

6. Build JNote:
    ```bash
    python3 -m PyInstaller JNote.spec
    ```

7. Run JNote:
    ```bash
    dist/JNote/JNote
    ```

#### Full Script

```bash
sudo apt-get update
sudo apt-get install git
git clone https://github.com/Dev-I-J/JNote.git
cd JNote
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.9
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
python3 -m pip install virtualenv
python3 -m virtualenv buildenv
source buildenv/bin/activate
python3 -m pip install PyInstaller
python3 -m pip install -r requirements.txt
python3 -m PyInstaller JNote.spec
dist/JNote/JNote
```