#markdown guide : https://www.markdownguide.org/cheat-sheet/

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latestearthquake-Indonesia",
    version="0.1",
    author="Deni Rahmawan",
    author_email="drahmawan0@gmail.com",
    description="This package will get the latest earthquake from BMKG | Meteorological, Climatological, and Geophysical Agency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Apatheia8/latest-Indonesia-earthquake",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    package=setuptools.find_packages(where="src"),
    python_requires='>=3.6',
)
