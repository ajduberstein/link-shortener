from __future__ import print_function

from fabric.api import local, task, settings


class FabricException(Exception):
    pass


@task
def check_dev_tools():
    with settings(abort_exception = FabricException):
        try:
            local('fswatch --version')
            local('tmux -V')
        except FabricException:
            print('You are missing one or more devtools')


@task
def frontend_dev():
    print('Running frontend build process')
    local('cd ./client && npm run build-copy:watch')


@task
def dev():
    print('Running server')
    local('./env/bin/python run.py')
