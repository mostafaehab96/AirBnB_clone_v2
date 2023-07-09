#!/usr/bin/python3
"""creates and distributes an archive to your web servers
using the functions do_deploy and do_pack."""

from fabric.api import local, run, env, put
from os import path
from datetime import datetime
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack


env.hosts = ['52.201.157.19', '100.26.230.29']
env.user = "ubuntu"


def deploy():
    """Creates an archive and deploy it on the servers."""

    # Creating the archive first
    path = do_pack()

    if path:
        return do_deploy(path)
