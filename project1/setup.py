try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My First Project',
    'author': 'Dave Spina',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dspina79@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['project1'],
    'script': [],
    'name': 'projectname'
}

setup(**config)