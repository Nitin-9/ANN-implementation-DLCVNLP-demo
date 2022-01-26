from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Nitin-9",
    author_email="er.nitintiwari548@gmail.com",
    description="A small package for ANN implimentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Nitin-9/ANN-implementation-DLCVNLP-demo",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
           "tensorflow",
           "matplotlib",
           "seaborn",
           "numpy",
           "pandas",
           "PyYAML"
   ]
)