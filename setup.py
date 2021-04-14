from distutils.core import setup

pkg = 'Extensions.NfsServer'
setup(name='enigma2-plugin-extensions-nfsserver',
       version='0.1',
       description='NFS Server',
       package_dir={pkg: 'plugin'},
       packages=[pkg]
      )
