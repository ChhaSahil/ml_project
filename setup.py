from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function return the requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('/n','') for req in requirements]
setup(
    author = "Sahil",
    author_email = 'sahilchhabra568@gmail.com',
    name = 'ml_project',
    packages = find_packages(),
    install_packages = get_requirements('requirements.txt')
)