# JNote - A Free NotePad

[![Build Status](https://travis-ci.org/Dev-I-J/JNote.svg?branch=master)](https://travis-ci.org/Dev-I-J/JNote)
[![Documentation Status](https://readthedocs.org/projects/jnote-notepad/badge/?version=latest)](https://jnote-notepad.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/license-GPL%203.0-green.svg)](https://opensource.org/licenses/GPL-3.0)
[![DeepSource](https://deepsource.io/gh/Dev-I-J/JNote.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/Dev-I-J/JNote/?ref=repository-badge)
[![Run on Repl.it](https://repl.it/badge/github/Dev-I-J/JNote)](https://repl.it/github/Dev-I-J/JNote)

![JNote Logo](icons/logo.png)

__JNote is a free NotePad__ application written in _Python and QML (PyQt5)._ Binaries are available for Windows and Mac, but you can _build from source_ for Linux (See Below).

## Features

The current version is v1.6.9 and additional for basic functions of a note pad, it can

* Automatically Check For Updates,
* Determine A File Is Binary Or Not And Show Message,
* Automatically Guess and Use A Files Encoding While Opening,
* Open the last opened file automatically when started,
* Save and use the last used fonts when started,
* Insert Date and Time,
* Render Text As `HTML` Or `Markdown` In A Browser,
* Execute Text In `cmd.exe` (Windows and Mac Only),
* Super Clean Code.

And Many More Cool Features...

## Download

Download [Here](https://github.com/Dev-I-J/JNote/releases/latest)

## Help

Available At [Github Discussions](https://github.com/Dev-I-J/JNote/discussions)

## Build From Source

__Assuming you already have _Python along with 'pip'_ and _Git_ installed on your computer__,

### Linux / Mac OS

1. Clone This Repo in: `git clone https://github.com/Dev-I-J/JNote`
2. Install `shovel`: `python3 -m pip install shovel`
3. `cd` to JNote: `cd JNote`
4. Build and Run App: `python3 -m shovel app.assembleAppRun`
5. Run App Afterwards: `python3 -m shovel app.runApp`

### Windows

1. Clone This Repo in: `git clone https://github.com/Dev-I-J/JNote`
2. Install `shovel`: `python -m pip install shovel`
3. `cd` to JNote: `cd JNote`
4. Build and Run App: `python -m shovel app.assembleAppRun`
5. Run App Afterwards: `python -m shovel app.runApp`

## Price

It's completely FREE and Open Source!

## License

JNote is licensed under the GNU GPLv3 Open Source License.

## Documentation

Available [Here](https://jnote-notepad.readthedocs.io/en/latest/).

## Additional Information

Additional Information about JNote

### Credits

* All The Icons are provided by [Icons8](https://icons8.com) For Free.
* [`pipenv`](https://pypi.org/project/pipenv) Is Used For Dependency Management.
* [`shovel`](https://pypi.org/project/shovel) Is Used To Make The Development Process Easier.
* [`flake8`](https://pypi.org/project/flake8) Is Used For Linting Code.
* [`rope`](https://pypi.org/project/rope) Is Used For Refactoring Code.
* [`autopep8`](https://pypi.org/project/autopep8) Is Used For Formatting Code.
* [`sphinx`](https://pypi.org/project/Sphinx/) Is Used To Generate Documentation.
* Code Hosted By [GitHub](https://github.com).
* Documentation Hosted By [ReadTheDocs](https://readthedocs.org).
* Continuous Integration (`CI/CD`) Provided By [Travis CI](https://travis-ci.org).
* The app is build with [`PyInstaller`](https://pypi.org/project/PyInstaller).
* Special Thanks to [VS Code](https://vscode.com) For Providing the Awesome Code Editor.

### Python Modules Used in Development

* [`PyQt5`](https://pypi.org/project/PyQt5/) for the GUI.
* [`requests`](https://pypi.org/project/requests/) for Pinging the GitHub API to check for updates.
* [`version-parser`](https://pypi.org/project/version-parser/) for Comparing Versions.
* [`py-gfm`](https://pypi.org/project/py-gfm/) GitHub Flavored Markdown Extension for `markdown` module.
* [`markdown`](https://pypi.org/project/markdown/) for Converting markdown from GitHub to HTML.
* [`toml`](https://pypi.org/project/toml/) for parsing the settings file.
* [`binaryornot`](https://pypi.org/project/binaryornot/) for _guessing_ if files are binary or not.
* [`cchardet`](https://pypi.org/project/cchardet/) for _guessing_ the file encoding.
* [`chardet`](https://pypi.org/project/chardet/) for backup plan if `cchardet` fails to determine the correct encoding.

## Coming Soon

These functionalities are scheduled to be shipped with the future major releases.

* Command Line Access,
* Auto Updating,
* Settings dialog to control your preferences,
* Dark Mode!!
