from setuptools import setup, find_packages

setup(
    name='plotting_lib',
    version='0.1.0',
    description='A simple plotting library for height vs weight analysis',
    author='DigitCoreTech',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
    ],
    python_requires='>=3.7',
)
