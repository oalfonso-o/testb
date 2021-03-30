from setuptools import setup, find_packages


def read_requirements(filename):
    with open(filename) as f:
        reqs = f.readlines()
    # filter comments and drop references to other requirements files
    return [r.strip() for r in reqs
            if r[0] != '#' and r[:4] != 'git+' and r[:2] != '-r']


def read_dependency_links(filename):
    with open(filename) as f:
        reqs = f.readlines()
    # filter comments and  drop references to other requirements files
    return [r.strip() for r in reqs
            if r[0] != '#' and r[:4] == 'git+' and r[:3] != '-r']


install_reqs = read_requirements('./requirements.txt')
dependency_links = read_dependency_links('./requirements.txt')


setup(
    name='testb',
    version='1.0.0',
    description='testb service',
    author='Oriol Alfonso',
    author_email='oriolalfonso91@gmail.com',
    packages=find_packages(),
    install_requires=install_reqs,
    dependency_links=dependency_links,
    data_files=[('.', ['requirements.txt', ])],
    zip_safe=False,
)
