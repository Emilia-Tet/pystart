from setuptools import setup, find_packages

# najpierw cd i nazwa paczki
# potem python setup.py sdist

setup(
    name = 'finances',
    version = '0.0.1',
    description = 'sample_description',
    packages = find_packages(exclude=['*.tests', 'tests'])
)