from setuptools import setup


setup(name='policy',
    version='1.0dev',
    url='http://localhost',
    license='Private',
    description='Policy',
    author='Jarn AS',
    author_email='info@jarn.com',
    long_description='',
    packages=['policy'],
    install_requires=[
        'setuptools',
        'Plone',
        'plone.app.caching',
        'plone.app.discussion',
        'plone.app.testing',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
    },
)
