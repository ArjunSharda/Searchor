from setuptools import setup, find_packages
import pathlib

project_dir = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (project_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="searchor",
    version="2.3.1",
    description="⚡️ Quick and easy search engine queries.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjunSharda/Searchor",
    author="Arjun Sharda",
    author_email="sharda.aj17@gmail.com",
    classifiers=[  # Optional
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    #keywords="sample, setuptools, development",
    
    package_dir={"": "src"},
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where="src"),  # Required

    python_requires=">=3.7, <4",

    install_requires=["pyperclip"],
    
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    
    #extras_require={  # Optional
    #    "dev": ["check-manifest"],
    #    "test": ["coverage"],
    #},
    
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        "console_scripts": [
            "searchor=searchor.main:cli",
        ],
    },
    project_urls={
    "Homepage":"https://github.com/ArjunSharda/Searchor",
    "Bug Tracker":"https://github.com/ArjunSharda/Searchor/issues"
    },
)
