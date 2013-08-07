from distutils.core import setup

setup(
    name="TreeHash",
    version="1.0pre",
    packages=['treehash'],
    scripts=['bin/treehash'],
    license="Simplified BSD",
    long_description=open('README.rst').read(),
    url="http://github.com/jdswinbank/treehash",
    author="John Swinbank",
    author_email="john@treehash.swinbank.org"
)
