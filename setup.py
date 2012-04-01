from setuptools import setup, find_packages

setup(
    name = 'negotiate',
    version = '0.0.1',
    packages = find_packages(),

    install_requires = [
        'decorator==3.3.2'
    ],
    extras_require = {
        'test': [
            'nose',
            'mock'
        ]
    },

    # metadata for upload to PyPI
    author = 'Nick Stenning',
    author_email = 'nick@whiteink.com',
    url = 'https://github.com/nickstenning/negotiate',
    description = 'Negotiate: smart, simple content negotiation for Python web applications',
    license = 'MIT',
    keywords = 'contenttype contentnegotiation http hypermedia'
)
