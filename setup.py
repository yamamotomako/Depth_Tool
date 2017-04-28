#! /usr/bin/env python

from setuptools import setup

setup(name="depth_tool",
	description="Calculating mean depth of bam attached to reference bed.",
	url="https://github.com/yamamotomako/depth_tool",
	package_dir={'':'scripts'},
	packages=["depth_tool"],
	scripts=["depth_tool"]
    )


