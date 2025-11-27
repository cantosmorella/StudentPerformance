from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .' # Editable mode of the requirements file
def get_requirements(file:str)->List[str]:
    # This function will return the list of requirements
    requirements = []
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name = 'student-performance-predict',
    version = '0.0.1',
    author = 'Cantos Morella',
    author_email = 'cantosmorella@gmail.com',
    packages = find_packages(), # Find all folders that are packages (directories with __init__.py)
    install_requires = get_requirements('requirements.txt')
)