import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "winontop",
    version = "0.3",
    author = "Jithu R Jacob",
    author_email = "jithurjacob@gmail.com",
    description = ("An easy tool to keep windows on top of others."),
    license = "BSD",
    keywords = "python windows top winontop windowsontop",
    url = "https://github.com/jithurjacob/winontop",
    download_url = 'https://github.com/jithurjacob/winontop/tarball/0.3',
    packages=['winontop'],
    entry_points = {
        "console_scripts": ['winontop = winontop.winontop:main']
        },
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: BSD License",
    ],
)
