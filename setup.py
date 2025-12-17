from setuptools import setup, find_packages

setup(
    name="kg-agent",
    version="0.1.0",
    description="Skeleton implementation of KG-Agent: an autonomous agent framework for KG reasoning",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "networkx>=3.0",
        "rdflib>=6.0.0",
    ],
)
