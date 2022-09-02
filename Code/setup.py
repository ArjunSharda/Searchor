from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 2 - Pre-Alpha',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9',
  'Programming Language :: Python :: 3.10'
]

setup(
  name='Searchor',
  version='1.1.1',
  description='Math package',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/ArjunSharda/Searchor',  
  author="Arjun Sharda",
  author_email='sharda.aj17@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Searchor', 
  packages=find_packages(),
  install_requires=[''] 
)
