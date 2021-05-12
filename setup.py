from setuptools import setup, find_packages

NAME = 'tonietools'

setup(
    name=NAME,
    version='0.0.1',
    description="TonieTools",
    url='https://github.com/floscha/tonietools',
    author='Florian Schäfer',
    author_email='florian.joh.schaefer@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=open("requirements.txt", "r").readlines(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'tonietools = tonietools.cli:app',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only'
    ]
)