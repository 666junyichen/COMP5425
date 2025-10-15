"""
Setup configuration for COMP5425 project.
"""

from setuptools import setup, find_packages

setup(
    name="comp5425-project",
    version="0.1.0",
    description="COMP5425 School Project",
    author="Add author name",
    author_email="Add author email",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        # Add project dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
        ],
    },
)
