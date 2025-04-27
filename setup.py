from setuptools import setup, find_packages

setup(
    name="project-mjolnir",
    version="2.1.0",
    author="DaveTmire85",
    description="A modular, cross-platform D&D 3.5e parser and database builder.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/project-mjolnir/",
    project_urls={
        "Source": "https://github.com/DaveTmire85/Project_Mjolnir",
        "Tracker": "https://github.com/DaveTmire85/Project_Mjolnir/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "python-docx>=0.8.11",
    ],
    include_package_data=True,
    zip_safe=False,
)
