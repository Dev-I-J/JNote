from shovel import task

from os import chdir
from shutil import rmtree
from os.path import abspath, join
from subprocess import run as shell
from webbrowser import open_new_tab


@task
def installDevDeps():
    shell("pip install pipenv")
    shell("pipenv install --dev")


@task
def cleanDoc():
    rmtree('docs/build', ignore_errors=True)


@task
def runDoc():
    open_new_tab(
        "file://{}".format(join(abspath("."), "docs/build/html/index.html"))
    )


@task
def buildDoc():
    chdir("docs")
    shell("pipenv run make html")
    chdir("../")


@task
def assembleDocRun():
    installDevDeps()
    cleanDoc()
    buildDoc()
    runDoc()
