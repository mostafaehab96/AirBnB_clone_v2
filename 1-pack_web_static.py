#!/usr/bin/python3
"""Defines a function that compresses the web_static folder using fabric."""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a tgz archive of web_static folder
    in a version folder.
    Return: the path of the archive if generated or None otherwise
    """
    time = datetime.now()  # For renaming the file
    time = time.strftime("%Y%m%d%H%M%S")
    filepath = f"versions/web_static_{time}.tgz"

    try:
        local("mkdir -p versions")
        result = local(f'tar -czvf {filepath} web_static')
        if result.succeeded:
            return filepath
        else:
            return None
    except:
        return None
