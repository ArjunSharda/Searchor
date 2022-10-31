from setuptools import setup, find_packages
import pathlib

project_dir = pathlib.Path(__file__).parent.resolve()
long_description = (project_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="searchor",
    version="2.4.2",
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

    
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # Required

    python_requires=">=3.7, <4",

    install_requires=["pyperclip", "aenum", "click"],
   
    
   
    entry_points={  
        "console_scripts": [
            "searchor=searchor.main:cli",
        ],
    },
    project_urls={
    "Homepage":"https://github.com/ArjunSharda/Searchor",
    "Bug Tracker":"https://github.com/ArjunSharda/Searchor/issues"
    },
)
