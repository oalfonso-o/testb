from setuptools import setup, find_packages

setup(
    name='testb',
    version='1.0.0',
    description='testb service',
    author='Oriol Alfonso',
    author_email='oriolalfonso91@gmail.com',
    packages=find_packages(),
    install_requires=['testa @ git+ssh://git@github.com/oalfonso-o/testa.git'],
    zip_safe=False,
)
