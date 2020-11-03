from setuptools import find_packages, setup


setup(
    name='gilded_rose',
    package_dir={'': 'src'},
    packages=find_packages(exclude=['tests*']),
    python_requires='>=3.7',
    zip_safe=True,
)
