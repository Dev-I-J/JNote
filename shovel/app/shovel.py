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
    shell(".test/dist/JNote/JNote")


@task
def cleanApp():
    """Clean PyInstaller Build Output"""
    rmtree('./build', ignore_errors=True)
    rmtree('./dist', ignore_errors=True)


@task
def cleanAppFolder(platform):
    """Clean PyInstaller Build Output"""
    if platform == "Mac":
        rmtree('./dist/JNote.app', ignore_errors=True)
    else:
        rmtree('./dist/JNote', ignore_errors=True)
    rmtree('./build', ignore_errors=True)


@task
def cleanAppDebug():
    """Clean PyInstaller Debug Build Output"""
    rmtree('./.test/build', ignore_errors=True)
    rmtree('./.test/dist', ignore_errors=True)
    rmtree('./.test/icons', ignore_errors=True)
    remove("./.test/fileio.py")
    remove("./.test/settings.py")
    remove("./.test/main.py")
    remove("./.test/main.qml")
    remove("./.test/settings.toml")
    remove("./.test/README.md")
    remove("./.test/LICENSE.md")


@task
def buildApp():
    """Build With PyInstaller"""
    shell(["pipenv", "run", "PyInstaller", "JNote.spec"])


@task
def buildAppDebug():
    """Build With PyInstaller With 'debug' and 'console' Flags On"""
    copyfile("./fileio.py", ".test/fileio.py")
    copyfile("./settings.py", ".test/settings.py")
    copyfile("./main.py", ".test/main.py")
    copyfile("./main.qml", ".test/main.qml")
    copyfile("./settings.toml", ".test/settings.toml")
    copyfile("./README.md", ".test/README.md")
    copyfile("./LICENSE.md", ".test/LICENSE.md")
    copytree("./icons", ".test/icons")
    chdir("./.test")
    shell(["pipenv", "run", "PyInstaller", "JNote.spec"])
    chdir("../")


@task
def publishApp(platform):
    """Put Builded Application In A Zip File Matching The Platform"""
    shell(["7z", "a", "JNote_{}.zip".format(platform), "./dist/*"])


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
def assembleAppPublish(platform, pip="pip"):
    """Install Dependencies, Clean, Build and Run Executable"""
    installDeps(pip)
    cleanApp()
    buildApp()
    publishApp(platform)
    cleanAppFolder(platform)
