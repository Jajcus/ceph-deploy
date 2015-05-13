from ceph_deploy.util import pkg_managers
from ceph_deploy.lib import remoto

def uninstall(conn, purge=False):
    packages = [
        'ceph',
        'ceph-radosgw',
        ]

    pkg_managers.poldek_remove(
        conn,
        packages,
    )
    remoto.process.run(
        conn,
        ['sh', '-c', 'rm -f /etc/systemd/system/ceph.target.wants/* || :']
    )
