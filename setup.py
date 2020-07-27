import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datastructure_collection-nyakaz73", # Replace with your own username
    version="0.0.1",
    author="Tafadzwa L Nyamukapa",
    author_email="tafadzwalnyamukapa@gmail.com",
    description="A DataStructure collection written in Pyhton which helps developers and big-data scientists in implementing fast and efficient algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nyakaz73/datastructure_collection.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)