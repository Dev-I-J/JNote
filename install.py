from sys import platform
import pip
import os

_all_ = [
    "toml",
    "PyQt5",
    "py-gfm",
    "charamel",
    "requests",
    "markdown",
    "version-parser",
]

windows = ["python-magic-bin"]

darwin = ["python-magic-bin"]

linux = ["python-magic"]


def install(packages):
    for package in packages:
        pip.main(['install', package])


if __name__ == '__main__':

    install(_all_)
    if platform == 'win32':
        install(windows)
    elif platform == "darwin":
        install(darwin)
    else:
        os.system("sudo apt-get install libmagic-dev")
        install(linux)
