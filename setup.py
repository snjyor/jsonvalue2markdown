from setuptools import setup
import os
abs_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(abs_path, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="jsonvalue2markdown",
    py_modules=["jsonvalue2markdown"],
    version="0.0.1",
    description="Convert json value to markdown",
    author="snjyor",
    author_email="snjyor@163.com",
    url="https://github.com/snjyor/jsonvalue2markdown",
    long_description=long_description,
    license="MIT",
    long_description_content_type="text/markdown"
)
