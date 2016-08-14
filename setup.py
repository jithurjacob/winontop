import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "winontop",
    version = "0.0.1",
    author = "Jithu R Jacob",
    author_email = "jithurjacob@gmail.com",
    description = ("An easy tool to keep windows on top of others."),
    license = "BSD",
    keywords = "python windows top winontop windowsontop",
    url = "http://packages.python.org/winontop",
    packages=['winontop'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
