from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return a list of requirements
    """
    # requirement_list:List[str] = []

    """Wrtite code to read requirements.txt file and append each requirement
       in requirement_list variable.
    """
    with open(r"requirements.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
    requirement_list = [line for line in all_lines]
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Prakash",
    author_email="aijpshm@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),  #['pymongo==4.2.0'],
)