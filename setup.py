from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Package for google sso login in FastAPI'
LONG_DESCRIPTION = 'Package for google sso login in FastAPI'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="fastapi_middlewares", 
        version=VERSION,
        author="Nicolas Acosta",
        author_email="nicolas.acosta@itutor.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            "Authlib==1.0.1", 
            "httpx==0.22.0", 
            "itsdangerous==2.1.2", 
            "jinja2==3.1.1", 
            "fastapi>=0.75.2", 
        ],
        url=["https://github.com/bcpitutor/fastapi_middlewares"],
        keywords=['google-sso', 'fastapi'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Engineers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Microsoft :: Ubuntu",
        ]
)