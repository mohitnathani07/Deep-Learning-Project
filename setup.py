from setuptools import find_packages, setup


def get_requirements(filepath):
    requirements = []
    with open(filepath) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="End to End Project",
    version="0.1", 
    author="Mohit",
    author_email="mohit.nathani2@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)