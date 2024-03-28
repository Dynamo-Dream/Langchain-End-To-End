# THis is used to install the local packages in Environments
# src folder is for source code
# __init__.py is used to treat this folder as Local package


from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements.
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Anish Kumar",
    author_email="theanish2002kumar@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)