#!/usr/bin/python3
"""python script"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    local("mkdir -p versions")
    now = datetime.now()
    file_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    try:
        local("tar -cvzf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except BaseException:
        return None
