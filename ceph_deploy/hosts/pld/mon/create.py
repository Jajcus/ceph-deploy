from ceph_deploy.hosts import common
from ceph_deploy.lib import remoto


def create(distro, args, monitor_keyring):
    hostname = distro.conn.remote_module.shortname()
    common.mon_create(distro, args, monitor_keyring, hostname)

    remoto.process.run(
        distro.conn,
        [
            'systemctl',
            'enable',
            'ceph-mon@{hostname}.service'.format(hostname=hostname)
        ],
        timeout=7,
    )
    remoto.process.run(
        distro.conn,
        [
            'systemctl',
            'start',
            'ceph-mon@{hostname}.service'.format(hostname=hostname)
        ],
        timeout=7,
    )
    remoto.process.run(
        distro.conn,
        [
            'ceph-create-keys',
            '--cluster', args.cluster,
            '-i', hostname,
        ],
        timeout=7,
    )
