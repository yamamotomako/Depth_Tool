#! /usr/bin/env python

<<<<<<< HEAD
from setuptools import setup

setup(name="depth_tool",
	#description="Calculating mean depth tool.",
	#url="https://github.com/yamamotomako/depth_tool",
	package_dir={'':'scripts'},
	packages=["depth_tool"],
	scripts=["depth_tool"]
=======
#from setuptools import setup
from distutils.core import setup

setup(name='depth_tool',
	description="Calculating mean depth tool.",
	url='https://github.com/yamamotomako/calc_mean_depth',
	package_dir={'': 'scripts'},
	packages=['depth_tool'],
	scripts=['depth_tool']
>>>>>>> d4d91516c3cb19bfb514970f1cdbcc3bed889d01
	)


