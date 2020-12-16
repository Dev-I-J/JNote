from shovel import task

from os import chdir, remove
from subprocess import run as shell
from shutil import rmtree, copyfile, copytree


@task
def installDeps(pipPath="pip"):
    """Install Dependencies"""
    shell([pipPath, "install", "--upgrade", "pipenv"])
    shell(["pipenv", "install", "--dev"])


@task
def runConsole():
    """Run App In Console (python)"""
    shell(["pipenv", "run", "python", "main.py"])


@task
def runWindow():
    """Run Application Without Console (pythonw)"""
    shell(["pipenv", "run", "pythonw", "main.py"])


@task
def runApp():
    """Run Executable Built By PyInstaller"""
    shell("dist/JNote/JNote")


@task
def runAppDebug():
    """Run Debug Executable Built By PyInstaller"""
    shell(".debug/dist/JNote/JNote")


@task
def cleanApp():
    """Clean PyInstaller Build Output"""
    rmtree('./build', ignore_errors=True)
    rmtree('./dist', ignore_errors=True)


@task
def cleanAppDebug():
    """Clean PyInstaller Debug Build Output"""
    rmtree('./.debug/build', ignore_errors=True)
    rmtree('./.debug/dist', ignore_errors=True)
    rmtree('./.debug/icons', ignore_errors=True)
    rmtree('./.debug/data', ignore_errors=True)
    remove("./.debug/signals.py")
    remove("./.debug/fileio.py")
    remove("./.debug/settings.py")
    remove("./.debug/main.py")
    remove("./.debug/main.qml")
    remove("./.debug/settings.toml")


@task
def buildApp():
    """Build With PyInstaller"""
    shell(["pipenv", "run", "PyInstaller", "JNote.spec"])


@task
def buildAppDebug():
    """Build With PyInstaller With 'debug' and 'console' Flags On"""
    copyfile("./signals.py", ".debug/signals.py")
    copyfile("./fileio.py", ".debug/fileio.py")
    copyfile("./settings.py", ".debug/settings.py")
    copyfile("./main.py", ".debug/main.py")
    copyfile("./main.qml", ".debug/main.qml")
    copyfile("./settings.toml", ".debug/settings.toml")
    copytree("./icons", ".debug/icons")
    copytree("./data", ".debug/data")
    chdir("./.debug")
    shell(["pipenv", "run", "PyInstaller", "JNote.spec"])
    chdir("../")


@task
def publishApp(platform, version):
    """Put Builded Application In A Zip File Matching The Platform"""
    if platform == "Mac":
        shell([
            "7z", "a", f"JNote_{platform}_{version}.zip",
            "./dist/JNote.app"
        ])
    else:
        if platform == "Windows_32bit":
            shell([
                "iscc", "inno_setup_32.iss"
            ])
        elif platform == "Windows_64bit":
            shell([
                "iscc", "inno_setup_64.iss"
            ])
        shell([
            "7z", "a", f"JNote_{platform}_{version}.zip",
            "./dist/JNote"
        ])


@task
def assembleConsoleRun(pip="pip"):
    """Install Dependencies and Run In Console"""
    installDeps(pip)
    runConsole()


@task
def assembleWindowRun(pip="pip"):
    """Install Dependencies and Run Without Console"""
    installDeps(pip)
    runWindow()


@task
def assembleAppRun(pip="pip"):
    """Install Dependencies, Clean, Build and Run Executable"""
    installDeps(pip)
    cleanApp()
    buildApp()
    runApp()


@task
def assembleAppPublish(platform, version, pip="pip"):
    """Install Dependencies, Clean, Build and Run Executable"""
    installDeps(pip)
    cleanApp()
    buildApp()
    publishApp(platform, version)
    cleanApp()
