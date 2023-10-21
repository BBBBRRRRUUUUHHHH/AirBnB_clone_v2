#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import *
import os
from datetime import datetime

env.hosts = ['52.86.110.104', '34.204.95.100']
env.user = 'ubuntu'

def do_pack():
    """
    Generates a .tgz archive from the
    contents of the web_static folder
    Returns:
    Path to the archive if successful, None otherwise
    """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(timestamp)
    print('Packing web_static to {}'.format(path))
    if local('{} && tar -cvzf {} web_static'.format(mkdir, path)).succeeded:
        return path
    return None

def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    Args:
        archive_path: Path to the archive file on the local machine
    Returns:
        True if all operations are successful, otherwise False
    """

    try:
        if not od.path.exists(archive_path):
            return False

