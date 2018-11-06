from setuptools import setup

setup(name='McClinton Python Package',
      version='0.1',
      description='Read a matrix and run BLAST searches',
      url='TBD',
      author='Sydnie McClinton',
      author_email='sydnie.mcclinton@selu.edu',
      license='MIT',
      packages=['mcclintonpythonpackage'],
      install_requires=[
          'dendropy',
          'pandas',
          'biopython'
      ],
      long_description=open('README.txt').read(),
zip_safe=True)