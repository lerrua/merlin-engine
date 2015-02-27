from setuptools import setup, find_packages

import merlin

classifiers = [
    'Development Status :: 1 - Planning'
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Environment :: Console',
    'Environment :: Plugins',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Games/Entertainment :: Role-Playing',
    'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
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
      url='https://www.github.com/lerrua/merlin-engine',
      license=merlin.__license__,
      packages=find_packages(exclude=('docs')),
      namespace_packages=['merlin'],
      package_dir={'merlin': 'merlin'},
      install_requires=['PyYAML'],
      include_package_data=True,
      zip_safe=False)
