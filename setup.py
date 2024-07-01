from setuptools import setup, find_packages

setup(
    name='carbon_footprint_calculator',
    version='0.1.0',
    description='A Python package to calculate carbon footprint from various activities.',
    author='Jinquan Ye',
    author_email='jinquan.ye@duke.edu',
    url='https://github.com/yebarryallen/SECFC',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'matplotlib>=3.0.0'
    ],
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
