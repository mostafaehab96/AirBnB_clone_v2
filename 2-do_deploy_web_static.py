#!/usr/bin/python3

"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers.
"""
from fabric.api import run, env, put
from os import path


env.hosts = ['52.201.157.19', '100.26.230.29']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Returns True if all operations have been done correctly,
    otherwise returns False.
    """
    if archive_path is None or not path.exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[1]  # Filename
        just_name = filename.split('.')[0]  # Filename without extension
        destpath = "/data/web_static/releases/{}".format(just_name)
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(destpath))
        run("tar xzf /tmp/{} -C {}".format(filename, destpath))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(destpath, destpath))
        run("rm -rf {}/web_static".format(destpath))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(destpath))
        print("New version deployed!")
        return True
    except Exception:
        return False

