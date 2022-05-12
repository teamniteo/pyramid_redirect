import os

# this is a hack to prevent an ugly bug when
# setuptools performs sys.modules restoration
import multiprocessing

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(here, "README.rst")).read()
changes = open(os.path.join(here, "CHANGES.rst")).read()


requires = [
    "pyramid>=1.3a6",
]

setup(
    name="pyramid_redirect",
    version="0.4",
    description="Small Pyramid extension for redirecting urls",
    long_description=readme + "\n" + changes,
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["pyramid_redirect"],
    install_requires=requires,
    author="Niteo",
    author_email="info@niteo.co",
    license="BSD",
    url="https://github.com/teamniteo/pyramid_redirect",
    keywords="pyramid redirect pylons web",
    tests_require=requires,
    test_suite="pyramid_redirect",
)
