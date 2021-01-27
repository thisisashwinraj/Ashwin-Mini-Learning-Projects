from setuptools import find_packages
from setuptools import setup

setup(
  name='PandoraNLP',
  version='1.0.0',
  description='Perform NLP Operations',
  author='Ashwin Raj',
  author_email='rajashwin812@gmail.com',
  packages==find_packages(exclude=('tests*',)),
  license='MIT License',
  keywords='Pandora NLP',
 )
