try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='archive',
    version="0.1",
    #description='',
    author="Ben O'Steen",
    author_email='benjamin.osteen@ouls.ox.ac.uk',
    #url='',
    install_requires=["Pylons>=0.9.6.1","rdflib==2.4.0","uuid","elementtree"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'archive': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'archive': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    entry_points="""
    [paste.app_factory]
    main = archive.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
