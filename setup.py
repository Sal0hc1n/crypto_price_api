# Copyright (C) 2015 Bitquant Research Laboratories (Asia) Limited
# Released under the Simplified BSD License

from setuptools import (
    setup,
    find_packages,
)

setup(
    name='cryptocurrency-price-api',
    version = '0.2',
    author='Anil Daoud',
    author_email='anil+git@via.ecp.fr',
    url='https://github.com/AnilDaoud/cryptocurrency-price-api',
    description="API's for cryptocurrencies exchanges",
    long_description='''Price API's for cryptycurrencies exchanges''',
    license='MIT',
    packages=['exchanges'],
    install_requires = ['requests', 'python-dateutil', 'websocket-client'],
    use_2to3 = True,
    include_package_data=True
)
