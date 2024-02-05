#!/usr/bin/python3
"""python script"""
from fabric.api import env, put, run
from os.path import exists
from fabric.api import local
from datetime import datetime

env.hosts = ['54.90.1.129', '18.208.119.233']


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


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        archv_no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, archv_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, archv_no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, archv_no_ext))
        run('rm -rf {}{}/web_static'.format(path, archv_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, archv_no_ext))
        return True
    except BaseException:
        return False


def deploy():
    """
    Creates and distributes an archive to your web servers,
    using the function deploy.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
