from setuptools import setup

version = '1.2.1'


setup(
    name='yogi',
    packages=['yogi'],
    install_requires=[''],
    package_data={"yogi": ["yogi.pyi"]},
    version=version,
    description='Simple typed interface to read input in Python',
    long_description='Simple typed interface to read input in Python',
    author='Jordi Petit',
    author_email='jpetit@cs.upc.edu',
    url='https://github.com/jutge-org/yogi',
    download_url=f'https://github.com/jutge-org/yogi/tarball/{version}',
    keywords=['yogi', 'education', 'input', 'read', 'scan'],
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Education',
    ],
)
