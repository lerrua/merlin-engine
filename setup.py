from setuptools import setup, find_packages

import merlin


classifiers = [
    'Development Status :: 5 - Production/Stable',
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    'Programming Language :: Python',
    "Programming Language :: Python :: 2.7",
    "Operating System :: OS Independent",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.rst').read()
except:
    long_description = merlin.__description__


setup(name='merlin',
      version=merlin.__version__,
      description=merlin.__description__,
      long_description=long_description,
      classifiers=classifiers,
      keywords='merlin rpg game engine',
      author=merlin.__author__,
      author_email=merlin.__email__,
      url='https://www.github.com/lerrua/merlin',
      download_url="https://github.com/merlin/merlin/tarball/master",
      license=merlin.__license__,
      packages=find_packages(exclude=('docs')),
      namespace_packages=['merlin'],
      package_dir={'merlin': 'merlin'},
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
