import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autoui",
    version="0.0.1",
    author="Erxin(Edwin) Shang",
    author_email="author@example.com",
    description="A Simplified UI automation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shangerxin/autoui",
    project_urls={
        "Bug Tracker": "https://github.com/shangerxin/autoui/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: Windows",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
