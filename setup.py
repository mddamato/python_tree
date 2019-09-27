from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='python_tree',
      url='https://github.com/mongoos2006/python_tree',
      author="Mike D",
      packages=find_packages(),
      install_requires=[
          'psutil'
      ],
      entry_points={
          'console_scripts': [
              'python_tree=python_tree.__main__:main'
          ],
      })
