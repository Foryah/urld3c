from distutils.core import setup

setup(
    name='urld3c',
    version='0.1',
    url='https://github.com/foryah/urld3c',
    licence='MIT',
    author='Foryah',
    description='Tool for url encoding/decoding the stdin',
    platforms='any',
    scripts=['bin/urld3c'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
