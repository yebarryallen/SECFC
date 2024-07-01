from setuptools import setup, find_packages

setup(
    name='carbon_footprint_calculator',
    version='0.1.0',
    description='A Python package to calculate carbon footprint from various activities.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/carbon_footprint_calculator',  # 修改为你的 GitHub 仓库地址
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'matplotlib>=3.0.0'  # 如果你使用了 matplotlib 来绘图
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # 修改为你选择的许可证
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
