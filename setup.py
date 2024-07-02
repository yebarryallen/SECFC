from setuptools import setup, find_packages

setup(
    name='SECFC',
    version='0.1.1',
    description='A Python package to calculate carbon footprint from various activities.',
    long_description= "The SECFC (Survey Embedded Carbon Footprint Calculator) is a Python package designed to calculate the carbon footprint of individuals based on their survey responses. This tutorial will guide you through using the package to calculate carbon footprints from survey data.",
    author='Jinquan Ye',
    author_email='jinquan.ye@duke.edu',
    url='https://github.com/yebarryallen/SECFC',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'matplotlib>=3.0.0'
    ],
    keywords=['survey', 'carbon footprint', 'emissions'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
