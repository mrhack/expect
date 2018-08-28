from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='expect',
    version=version,
    description='Python validate tool for json or other else',
    keywords='python expect json validate',
    author='mrhack',
    author_email='hdg1988@gmail.com',
    maintainer='mrhack',
    maintainer_email='hdg1988@gmail.com',
    url='https://github.com/mrhack/expect',
    platforms=["all"],
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ]
)
