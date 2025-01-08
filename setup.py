"""
This module contains the setup configuration for the Python package.

The setup.py file is essential for every end-to-end project because it serves several important purposes:
1. Package Distribution: It allows the project to be packaged and distributed to others, making it easy to share and install.
2. Dependency Management: It specifies the dependencies required by the project, ensuring that all necessary packages are installed.
3. Metadata: It provides metadata about the project, such as the name, version, author, and description, which is useful for users and tools.
4. Entry Points: It can define entry points for command-line interfaces or other scripts, making it easier to run the project.
5. Installation: It facilitates the installation process, allowing users to install the project using standard tools like pip.

Overall, the setup.py file is a crucial component for managing and distributing Python projects effectively.
"""

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:

    """
    Reads the requirements.txt file and returns a list of dependencies.

    This function opens the requirements.txt file, reads its contents,
    and splits the contents into a list of strings, where each string
    represents a dependency required by the project.

    Returns:
        List[str]: A list of dependencies specified in the requirements.txt file.
    """


    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst
        
setup(
    name="NetworkSecurity",
    version="0.1",
    author="Siddhartha Shrivastva",
    author_email="sidvastva@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)