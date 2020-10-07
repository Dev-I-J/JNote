
# ░█████╗░░█████╗░███╗░░░███╗██████╗░██████╗░███████╗░██████╗
# ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝
# ██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██████╔╝█████╗░░╚█████╗░
# ██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗
# ╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║░░██║███████╗██████╔╝
# ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░


# ▄▀█   █▀▀ █▀█ █▀▀ █▀▀   ▄▀█ █░█ ▀█▀ █▀█ █▀▄▀█ ▄▀█ ▀█▀ █ █▀▀
# █▀█   █▀░ █▀▄ ██▄ ██▄   █▀█ █▄█ ░█░ █▄█ █░▀░█ █▀█ ░█░ █ █▄▄

# █▀▀ ▀▄▀ █▀▀ █▀▀ █░█ ▀█▀ ▄▀█ █▄▄ █░░ █▀▀
# ██▄ █░█ ██▄ █▄▄ █▄█ ░█░ █▀█ █▄█ █▄▄ ██▄

# █▀▀ █▀█ █▀▄▀█ █▀█ █▀█ █▀▀ █▀ █▀ █▀▀ █▀█   █░█ █▀ █ █▄░█ █▀▀   █░█ █▀█ ▀▄▀
# █▄▄ █▄█ █░▀░█ █▀▀ █▀▄ ██▄ ▄█ ▄█ ██▄ █▀▄   █▄█ ▄█ █ █░▀█ █▄█   █▄█ █▀▀ █░█

# 🄸🄽🅂🅃🅁🅄🄲🅃🄸🄾🄽🅂 🄵🄾🅁 🅄🅂🄴
#     1. Open a Terminal or a Command Prompt.
#     2. Execute COMpres! ("compres -h" for help).

# 🄲🄷🄰🄽🄶🄴🄻🄾🄶
#     v1.0.0 - 2020/08/28
#         * Initial Release!

# 🅃🄾🄳🄾
#    * Decompress
#    * Config
#    * GUI

# 🄻🄸🄲🄴🄽🅂🄴
#    https://www.gnu.org/licenses/gpl-3.0-standalone.html

from os.path import join, abspath, dirname, relpath, normpath
from argparse import ArgumentParser, Namespace
from os import chdir, walk, system
from typing import List
import sys


def resource_path(relative_path: str) -> str:
    """ Get absolute path to resource, works for PyInstaller """
    base_path: str = sys._MEIPASS  # type: ignore
    return normpath(join(base_path, relative_path))


def getFiles(dirpath: str) -> List[str]:
    """Get Files From Given Directory"""
    files: List[str] = []

    for root, fol, theFile in walk(dirpath):

        for filename in theFile:
            rel_dir: str = relpath(root, dirpath)
            files.append(join(rel_dir, filename))

    return files


def run(
        path: str,
        ignored: List[str],
        ext: List[str],
        upath: str,
        level: str,
        verbose: bool
        ) -> None:
    """Main Function to Run"""
    getFile: List[str] = getFiles(path)
    v_opt: str = "-q"

    if verbose:
        v_opt = "-v"

    for theFile in getFile:
        if theFile in ignored:
            continue
        elif any(theFile.startswith(dirs + "\\") for dirs in ignored_files):
            continue
        elif not any(theFile.endswith('.' + extensions) for extensions in ext):
            continue
        else:
            chdir(path)
            command: str = "{} {} {} {}".format(upath, level, v_opt, theFile)
            system(command)


upx_path: str = ""
ulevel: str = ""

ignored_files: List[str] = [
    "./VCRUNTIME140.dll",
    "./VCRUNTIME140_1.dll",
    "./python3.dll",
    "./MSVCP140.dll",
    "./MSVCP140_1.dll",
    "./select.pyd",
    "PyQt5/Qt"
]

extensions: List[str] = [
    "dll",
    "exe",
    "pyd",
    "so",
    "lib",
    "dylib"
]

if getattr(sys, 'frozen', False):
    chdir(dirname(sys.executable))
    upx_path = resource_path('upx')
elif __file__:
    if dirname(__file__):
        chdir(dirname(__file__))
    upx_path = abspath('upx')
else:
    sys.exit()

commandParser: ArgumentParser = ArgumentParser(
    prog="compres",
    description="COMpres - A Free Automatic Executable Compresser Using UPX"
)

commandParser.add_argument(
    dest="path",
    help="Path to the Directory containing the Executables To Compress"
)

commandParser.add_argument(
    "--upx-path", "-u", dest="upx_path", default=upx_path, help="Path to UPX"
)

commandParser.add_argument(
    "--level", "-l", dest="level", default="9", help="UPX Compression Level",
    choices=["1", "2", "3", "4", "5", "6", "7", "8",
             "9", "best", "brute", "ultra-brute"]
)

commandParser.add_argument(
    "--verbose", "-v", dest="verbose", action="store_true", help="Be Verbose"
)

commandParser.add_argument(
    "--exclude", "-e", dest="exclude", default=[], nargs="+",
    help="Exclude Files"
)

commandParser.add_argument(
    "--add-ext", "-a", dest="add_ext", default=[], nargs="+",
    help="Add Custom Extensions"
)

args: Namespace = commandParser.parse_args()

if len(args.level) == 1:
    ulevel = "-" + args.level
else:
    ulevel = "--" + args.level

run(
    path=args.path,
    ignored=ignored_files + args.exclude,
    ext=extensions + args.add_ext,
    upath=args.upx_path,
    level=ulevel,
    verbose=args.verbose
)
