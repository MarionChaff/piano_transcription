from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name="thepkg",
    version="0.0.10",
    description="a package I created",
    license="MIT",
    author="Ahmed T. Hammad",
    author_email="ahmed.t.hammad@dbs.com",
    # url="https://github.com/",
    install_requires=requirements,
    packages=find_packages(),
    test_suite="tests",
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    zip_safe=False,
)
