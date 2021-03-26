"""
===============================================
vidgear library source-code is deployed under the Apache 2.0 License:

Copyright (c) 2019-2020 Abhishek Thakur(@abhiTronix) <abhi.una12@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
===============================================
"""
# import the necessary packages
import json
import sys
import platform
import setuptools
import urllib.request

from pkg_resources import parse_version
from distutils.util import convert_path
from setuptools import setup


def test_opencv():
    """
    This function is workaround to
    test if correct OpenCV Library version has already been installed
    on the machine or not. Returns True if previously not installed.
    """
    try:
        # import OpenCV Binaries
        import cv2

        # check whether OpenCV Binaries are 3.x+
        if parse_version(cv2.__version__) < parse_version("3"):
            raise ImportError(
                "Incompatible (< 3.0) OpenCV version-{} Installation found on this machine!".format(
                    parse_version(cv2.__version__)
                )
            )
    except ImportError:
        return True
    return False


def latest_version(package_name):
    """
    Get latest package version from pypi (Hack)
    """
    url = "https://pypi.python.org/pypi/%s/json" % (package_name,)
    try:
        response = urllib.request.urlopen(urllib.request.Request(url), timeout=1)
        data = json.load(response)
        versions = data["releases"].keys()
        versions = sorted(versions)
        return ">={}".format(versions[-1])
    except:
        pass
    return ""


pkg_version = {}
ver_path = convert_path("vidgear/version.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), pkg_version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    long_description = long_description.replace(  # patch for images
        "docs/overrides/assets", "https://abhitronix.github.io/vidgear/assets"
    )
    # patch for unicodes
    long_description = long_description.replace("➶", ">>")
    long_description = long_description.replace("©", "(c)")

setup(
    name="vidgear",
    packages=["vidgear", "vidgear.gears", "vidgear.gears.asyncio"],
    version=pkg_version["__version__"],
    description="High-performance cross-platform Video Processing Python framework powerpacked with unique trailblazing features.",
    license="Apache License 2.0",
    author="Abhishek Thakur",
    install_requires=[
        "pafy{}".format(latest_version("pafy")),
        "mss{}".format(latest_version("mss")),
        "numpy",
        "youtube-dl{}".format(latest_version("youtube-dl")),
        "streamlink{}".format(latest_version("streamlink")),
        "requests",
        "pyzmq{}".format(latest_version("pyzmq")),
        "colorlog",
        "colorama",
        "tqdm",
        "pyscreenshot{}".format(latest_version("pyscreenshot")),
        "Pillow",
    ]
    + (["opencv-python"] if test_opencv() else [])
    + (["picamera"] if ("arm" in platform.uname()[4][:3]) else []),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="abhi.una12@gmail.com",
    url="https://abhitronix.github.io/vidgear",
    extras_require={
        "asyncio": [
            "starlette{}".format(latest_version("starlette")),
            "aiofiles",
            "jinja2",
            "aiohttp",
            "uvicorn{}".format(latest_version("uvicorn")),
            "msgpack_numpy",
        ]
        + (
            ["uvloop"]
            if (platform.system() != "Windows" and sys.version_info[:2] >= (3, 7))
            else []
        )
    },
    keywords=[
        "OpenCV",
        "multithreading",
        "FFmpeg",
        "picamera",
        "starlette",
        "mss",
        "pyzmq",
        "uvicorn",
        "uvloop",
        "pafy",
        "youtube-dl",
        "asyncio",
        "dash",
        "streamlink",
        "Video Processing",
        "Video Stablization",
        "Computer Vision",
        "Video Streaming",
        "raspberrypi",
        "YouTube",
        "Twitch",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Multimedia :: Video",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    scripts=[],
    project_urls={
        "Bug Reports": "https://github.com/abhiTronix/vidgear/issues",
        "Funding": "https://ko-fi.com/W7W8WTYO",
        "Source": "https://github.com/abhiTronix/vidgear",
    },
)
