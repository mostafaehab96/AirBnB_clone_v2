#!/usr/bin/python3
"""Deletes the old versions of the archives of web_static
based on a number passed: deletes all - num."""

from fabric.api import env, run, local

env.hosts = ['52.201.157.19', '100.26.230.29']
env.user = "ubuntu"

# A variable to check that the code is run on localhost once
did_run = False


def do_clean(number=0):
    """The functions that cleans the archives."""

    global did_run
    # First deletes archives in local (once)!
    if not did_run:
        try:
            archives = local('ls -ltr versions', capture=True).split('\n')[1::]
            archives = [archive.split()[-1] for archive in archives]
            count = len(archives)
            number = int(number)

            # Deletes all - number archives in local
            if number > 1 and count > number:
                for i in range(count - number):
                    local('rm versions/{}'.format(archives[i]))
            elif count > 1 and count > number:
                for i in range(count - 1):
                    local('rm versions/{}'.format(archives[i]))
            did_run = True
        except Exception as e:
            print(e)

    # Delete the folders in /data/web_static/releases in remote
    remote = '/data/web_static/releases'
    try:
        archives = run('ls -ltr {}'.format(remote)).split('\n')[1::]
        archives = [archive.split()[-1] for archive in archives
                    if not archive.count('test')]
        count = len(archives)
        number = int(number)

        # Deletes all - number archives in remote
        if number > 1 and count > number:
            for i in range(count - number):
                run('rm -rf {}/{}'.format(remote, archives[i]))
        elif count > 1 and count > number:
            for i in range(count - 1):
                run('rm -rf {}/{}'.format(remote, archives[i]))
    except Exception:
        pass
