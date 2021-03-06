import setuptools

setuptools.setup(
    name="coinsta",
    version="0.0.1",
    url="https://github.com/PyDataBlog/Coinsta",

    author="Bernard Brenyah",
    author_email="bbrenyah@gmail.com",

    description="A Python package for acquiring both historical and current data of cryptocurrencies",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        'pandas>=0.23.1',
        'lxml>=4.2.2',
        'requests>=2.19.1'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
