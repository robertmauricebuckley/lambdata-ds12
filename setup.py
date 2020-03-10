# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdatas-ds12",
    version="1.0",
    author="Robert Buckley",
    author_email="robertworkbuckley@gmail.com",
    description="Practice packaging",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/robertworkbuckley/lambdata-ds12",
    # keywords="practice package",
    packages=find_packages() # ["game_utils"]
)