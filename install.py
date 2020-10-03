from sys import platform
import pip

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
    if platform == 'windows':
        install(windows)
    elif platform == "darwin":
        install(darwin)
    else:
        install(linux)
