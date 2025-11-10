from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:

    '''

        This function will return a list of requirements
        
    '''
    requirements_list:List[str]=[]
    try:

        with open ('requirements.txt','r') as file:
            # Read line from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirements=line.strip()
                #ignore empty lines and -e .
                if requirements and requirements!= "-e .":
                    requirements_list.append(requirements)
    
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirements_list

setup(
    name='Network Security',
    version="0.0.1",
    author='Anurag Verma',
    author_email='onuverma04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)




