from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]


    return requirements


setup(
    name='First ML Project',
    version='0.01',
    author='Maria Khan',
    author_email='mariakhan200502@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)





