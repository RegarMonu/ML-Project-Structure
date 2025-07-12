# So with the help of setup.py, I will be able to build my entire machine learning application as a package
# and even deploy in py py right. So python py py which we basically saw. And from there anybody can do the 
# installation and anybody can also use it.  So that is the reason why we specifically use setup.py okay.
from setuptools import find_packages, setup
from typing import List

def find_requirements(file_path: str) -> List[str]:
    '''
    Returns a list of required libraries from the given requirements file,
    excluding editable installs like '-e .'.
    '''
    HYPHEN_E_DOT = '-e .'
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip() and line.strip() != HYPHEN_E_DOT]
    
setup(
    name='generalStructure',
    version='0.0.1',
    author='Mahaveer Regar',
    author_email='mriasgyani@gmail.com',
    packages=find_packages(),
    install_requires = find_requirements('requirements.txt')
)