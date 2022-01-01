import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vis3dvf",
    version="1.0.0",
    description="Derivative of vis3dpy, aimed at visualizing ℝ³ vector fields ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/LukasDrsman/vis3dvf",
    author="Lukáš Dršman",
    author_email="lukaskodr@gmail.com",
    license="Public Domain",
    classifiers=[
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["vis3dvf"],
    include_package_data=True,
    install_requires=["numpy", "pygame", "PyOpenGL", "PyOpenGL_accelerate"],
    entry_points={},
)
