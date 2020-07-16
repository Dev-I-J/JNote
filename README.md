# JNote - A Free NotePad

__JNote is a free NotePad__ application written in _Python and QML. (PyQt5)_

## Features

The current version is v1.1.0 and additional for basic functions of a note pad, it can

* Automatically Check For Updates,
* Open the last opened file automatically when started,
* Catches errors effectively,
* Super Clean Code.

And So On...

## Download

JNote only supports Windows 64bit at this time. Support for other platforms may come soon!

* [Windows 64bit](https://github.com/Dev-I-J/JNote/releases/download/v1.1.0/JNote-Windows-64bit-v1.1.0.zip) - https://github.com/Dev-I-J/JNote/releases/download/v1.1.0/JNote-Windows-64bit-v1.1.0.zip

## Build From Source

__Assuming you already have _Python along with 'pip'_ and _Git_ installed on your computer__,

### Linux / Mac OS

1. Clone This Repo in Terminal: `git clone https://github.com/Dev-I-J/JNote`
2. Install Dependencies: `pip install -r requirements.txt`
3. Install PyInstaller: `pip install PyInstaller`
4. `cd` to JNote: `cd JNote`
5. Build the Python File: `PyInstaller --name "JNote" --icon "Icons/favicon.ico" --add-data "main.qml;." --add-data "log.txt;." --add-data "Icons;Icons" --clean --noconsole main.py`
6. Go to the directory where you cloned the repo in the file manager, and you will find a folder called dist, and in there, another one called JNote. The Executable will be inside it.

### Windows

1. Clone This Repo in CMD: `git clone https://github.com/Dev-I-J/JNote`
2. Install Dependencies: `pip install -r requirements.txt`
3. Install PyInstaller: `pip install PyInstaller`
4. `cd` to JNote: `cd JNote`
5. Build the Python File: `PyInstaller --name "JNote" --icon "Icons\favicon.ico" --add-data "main.qml;." --add-data "log.txt;." --add-data "Icons;Icons" --clean --noconsole main.py`
6. Go to the directory where you cloned the repo in the file explorer, and you will find a folder called dist, and in there, another one called JNote. The Executable will be inside it.

## Price

It's completely FREE and Open Source!

## License

JNote is licensed under the GNU GPLv3 Open Source License.

## Additional Information

Additional Information about jnote

### Credits

* All The Icons are provided by [Icons8](https://icons8.com).
* The app is build with [PyInstaler](https://pypi.org/project/PyInstaller)
* Special Thanks to [Atom](https://atom.io) for providing the awesome Editor.

### Python Modules Used in Development

* [PyQt5](https://pypi.org/project/PyQt5/) for the GUI.
* [requests](https://pypi.org/project/requests/) for Pinging the GitHub API to check for updates.
* [version-parser](https://pypi.org/project/version-parser/) for Comparing Versions.
* [markdown](https://pypi.org/project/markdown) for Converting markdown from GitHub to HTML.

## Coming Soon!

These functionality is scheduled to be shipped with the future major releases.

* Command Line Access,
* Auto Updating,
* Settings dialog to control your preferences,
* Dark Mode!!
