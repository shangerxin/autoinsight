import setuptools

from os.path import dirname, join


current_path = dirname(__file__)

with open(join(current_path, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open(join(current_path, "requirements.txt"), "r", encoding="utf=8") as fh:
    requires = fh.readlines()


def get_version(rel_path):
    with open(rel_path) as fh:
        for line in fh.readlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="autoinsight",
    version=get_version("src/autoinsight/__init__.py"),
    author="Erxin(Edwin) Shang",
    author_email="author@example.com",
    description="A Simplified UI automation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shangerxin/autoinsight",
    project_urls={
        "Bug Tracker": "https://github.com/shangerxin/autoinsight/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=requires,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={
        "": ["*.txt"]
    },
    data_files=["requirements.txt"]
)
