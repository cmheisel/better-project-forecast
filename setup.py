import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "better-project-forecast",
    version = "0.0.5",
    author = "Chris Heisel",
    author_email = "chris@heisel.org",
    description = ("Predict how long projects will take using monte carlo simulation"),
    license = "MIT",
    keywords = "monte carlo simulation project forecast",
    url = "https://github.com/cmheisel/better-project-forecast",
    packages=['better', 'tests'],
    long_description=read('README.md'),
    install_requires=["numpy==1.11.2", ],
    setup_requires=['pytest-runner==2.9', ],
    tests_require=['pytest==3.0.3', "pytest-flake8==0.8.1"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
