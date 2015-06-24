from setuptools import setup

setup(
    name='bartek-date-calculator',
    version='1.0.2',
    py_modules=['age2'],
    entry_points={
        'console_scripts': [
            'bdc = age2:main'
        ]
    }
)
