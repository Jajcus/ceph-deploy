import sys

from ceph_deploy.lib import remoto

def install(distro, version_kind, version, adjust_repos):
    logger = distro.conn.logger
    release = distro.release
    machine = distro.machine_type

    if version_kind not in ['stable', 'testing']:
        logger.error("Only 'stable' and 'testing' supported for PLD")
        sys.exit(1)

    if version_kind == 'testing':
        sources = ['-n', 'th-test', '-n', 'th-ready', '-n', 'th']
    else:
        sources = ['-n', 'th']

    remoto.process.run(
        distro.conn,
        [ 'poldek' ] + sources + [
            '--cmd',
            'install',
            'ceph',
            'ceph-radosgw',
        ],
    )
