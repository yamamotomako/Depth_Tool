#! /usr/bin/env python

from setuptools import setup

setup(name='depth_tool',
	description="Calculating mean depth tool.",
	url='https://github.com/yamamotomako/calc_mean_depth',
	package_dir={'': 'scripts'},
	packages=['depth_tool'],
	scripts=['depth_tool']
	)


