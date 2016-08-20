from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
        name='stockfighter'
        version='0.0.1-SNAPSHOT'
        description='Stockfighter challenge code'
        long_description=readme,
        author='Cully West',
        url='https://github.com/supwets/bayes_net',
        license=license,
        packages=find_packages(exclude=('tests', 'docs'))
)
