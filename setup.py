import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oplab-client-python",
    version="0.2.6",
    author="César Vargas",
    author_email="cesar@oplab.com.br",
    description="Oplab's API Client Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oplab-team/oplab-client-python",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.5',
)
