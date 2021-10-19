from setuptools import find_packages, setup


setup(
    package_dir={'': 'src'},
    packages=find_packages(exclude=['tests*']),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
