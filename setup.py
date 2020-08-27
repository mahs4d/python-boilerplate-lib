from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    # region core
    name="mypackage",
    version="0.0.0",
    python_requires=">=3.5",
    packages=find_packages(exclude=["scripts"]),
    install_requires=[],
    extras_require={
        "dev": [
            "appdirs==1.4.4",
            "attrs==20.1.0",
            "black==19.10b0; python_version >= '3.6'",
            "bleach==3.1.5",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2020.6.20",
            "cffi==1.14.2",
            "chardet==3.0.4",
            "click==7.1.2",
            "colorama==0.4.3",
            "cryptography==3.1",
            "distlib==0.3.1",
            "docutils==0.16",
            "idna==2.10",
            "importlib-metadata==1.7.0; python_version < '3.8'",
            "jeepney==0.4.3; sys_platform == 'linux'",
            "keyring==21.3.1",
            "orderedmultidict==1.0.1",
            "packaging==20.4",
            "pathspec==0.8.0",
            "pep517==0.8.2",
            "pip-shims==0.5.3",
            "pipenv-setup==3.1.1",
            "pipfile==0.0.2",
            "pkginfo==1.5.0.1",
            "plette[validation]==0.2.3",
            "pycparser==2.20",
            "pygments==2.6.1",
            "pyparsing==2.4.7",
            "python-dateutil==2.8.1",
            "readme-renderer==26.0",
            "regex==2020.7.14",
            "requests==2.24.0",
            "requests-toolbelt==0.9.1",
            "requirementslib==1.5.13",
            "rfc3986==1.4.0",
            "secretstorage==3.1.2; sys_platform == 'linux'",
            "six==1.15.0",
            "toml==0.10.1",
            "tomlkit==0.7.0",
            "tqdm==4.48.2",
            "twine==3.2.0",
            "typed-ast==1.4.1",
            "typing==3.7.4.3; python_version < '3.7'",
            "urllib3==1.25.10",
            "vistir==0.5.2",
            "webencodings==0.5.1",
            "wheel==0.35.1",
            "zipp==3.1.0; python_version < '3.8'",
        ]
    },
    dependency_links=[],
    # endregion
    # region data & scripts
    package_data={"mypackage": ["data/*"]},
    entry_points={"console_scripts": ["mypackage-cli = mypackage.bin.cli:main"]},
    # endregion
    # region metadata
    description="A sample Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahs4d/python-boilerplate-lib/",
    author="Mahdi Sadeghi",
    author_email="mail2mahsad@gmail.com",
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="sample setuptools development",
    project_urls={
        "Bug Reports": "https://github.com/mahs4d/python-boilerplate-lib/issues",
        "Source": "https://github.com/mahs4d/python-boilerplate-lib/",
    },
    # endregion
)
