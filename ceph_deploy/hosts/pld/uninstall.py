from ceph_deploy.util import pkg_managers


def uninstall(conn, purge=False):
    packages = [
        'ceph',
        'ceph-common',
        'radosgw',
        ]

    pkg_managers.poldek_remove(
        conn,
        packages,
    )

