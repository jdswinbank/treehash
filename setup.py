from distutils.core import setup

setup(
    name="TreeHash",
    version="1.0.1",
    packages=['treehash'],
    scripts=['bin/treehash'],
    license="Simplified BSD",
    description="Tree Hash Calculator",
    long_description=open('README.rst').read(),
    url="http://github.com/jdswinbank/treehash",
    author="John Swinbank",
    author_email="john@treehash.swinbank.org"
)
