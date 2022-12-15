import setuptools

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="rustkit",
    version="0.0.1",
    license="GNU",
    author="ddjerqq",
    author_email="ddjerqq@gmail.com",
    url="https://github.com/ddjerqq/rustkit",
    keywords="rust optional result iterator vector",
    description="A Rust toolkit library for python which allows you to write rust-like code in python.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["src"],
)
