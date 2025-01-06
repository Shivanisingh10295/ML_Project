from setuptools import find_packages, setup
from typing import List

HYPENDOT = '-e .'

def setup_requirements(file_path: str) -> List[str]:
    """This function will return a list of requirements from the specified file."""
    requirement = []
    with open(file_path) as file_object:
        requirement = file_object.readlines()
        requirement = [req.strip() for req in requirement if req.strip()]  # Remove empty lines and spaces

    # Remove '-e .' entry if it exists
    requirement = [req for req in requirement if req != HYPENDOT]

    return requirement

setup(
    name="ML_Project",
    version="0.0.1",
    author="Shivani Singh",
    author_email="shivani.singh10295@gmail.com",
    packages=find_packages(),
    install_requires=setup_requirements('requirement.txt')  # Ensure the list is clean
)
