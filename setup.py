import pathlib
from io import open
from os import path

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs
                    if 'git+' not in x]

setup(
    name='MyCart',
    description='A simple commandline app for products in cart',
    version='1.0.0',
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3',
    entry_points='''
        [console_scripts]
        mycart=MyCart.__main__:main
    ''',
    author="Gaurav Dabhade",
    keyword="products, mycart, e-commers",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/gauravndabhade/MyCart',
    download_url='https://github.com/gauravndabhade/MyCart',
    dependency_links=dependency_links,
    author_email='gauravndabhade@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)