# python-boilerplate-lib

simple boilerplate for python packages.

# Package

the package code goes into `mypackage` directory. you can change it's name :)

# Scripts

put you scripts in mypackage/bin directory and add them to `entry_points` of `setup.py`.

# Data Files

all files in `mypackage/data` directory will be added to the package.
you can use them through `pkg_resources.resource_filename('mypackage', 'data/xxxxx')`.

# Publish

to publish you package do the following 

```shell script
pipenv run sync
pipenv run build
pipenv run publish
pipenv run clean
```
