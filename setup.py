import io
import os

from setuptools import find_packages, setup


def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="YouSum",
    version=read(".", "VERSION"),
    description="yousum - summarize youtube videos with GPT and Whisper",
    url="https://github.com/padiauj/yousum",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Umesh Padia",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    scripts=["bin/yousum"],
)
