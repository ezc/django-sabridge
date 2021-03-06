from setuptools import setup, find_packages

# get around issues importing sqlalchemy
execfile('sabridge/version.py')

tests_require = [
    'Django>=1.2,<1.4',
]
setup(
    name='django-sabridge',
    version=__version__,
    author='John Paulett',
    author_email='john@paulett.org',
    url='https://django-sabridge.readthedocs.org',
    description = 'Provides SQLAlchemy access to Django models.',
    license='BSD',
    packages=find_packages(exclude=('tests',)),
    zip_safe=True,
    install_requires=[
        'sqlalchemy>=0.6.0',
    ], 
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Software Development'
    ],
)
