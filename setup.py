from sys import version

from distutils.core import setup
setup(name='paho-mqtt',
	version='0.4.91',
	description='MQTT version 3.1 client class',
	author='Roger Light',
	author_email='roger@atchoo.org',
	url='http://eclipse.org/paho',
	license='Eclipse Public License v1.0 / Eclipse Distribution License v1.0',
    package_dir={'': 'src'},
    packages=['paho', 'paho.mqtt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Internet',
        ]
	)
