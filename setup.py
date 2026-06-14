from setuptools import find_packages,setup 
#find-packages helps python to find all folders inside a project automatically and setup tools tells all information about our project 

from typing import List #this line just import list from typing module to return output of function as list 
HYPEN_E_DOT='-e .'#just a variable
def get_requirements(file_path:str)->List[str]:#this function just get a file and will returns output according to function body 
    '''
    this function will return the list of requirements'''
    requirements=[]#just an empty list later will puts something inside it 
    with open(file_path) as file_obj:#open file read it and store info in file_obj and automatically close it bcz of with 
        requirements=file_obj.readlines()#read every line 
        requirements=[req.replace("\n","") for req in requirements]#bcz each line moving to next has /n so remove it 
        if HYPEN_E_DOT in requirements:#in requirement if we have .e it will also added in list so remove it

            requirements.remove(HYPEN_E_DOT)
    return requirements#give the final list back 

setup(
name="mlproject",
version="0.01",
author="Zainab Riaz",
author_email='zainabriaz909@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)
