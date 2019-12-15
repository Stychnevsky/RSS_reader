from setuptools import setup
from setuptools import find_packages

setup(
    name='rss_reader',
    version='1.0',
    description='RSS reader',
    author='Anton Stychnesky',
    author_email='stychnevsky@gmail.com',
    url='https://github.com/Stychnevsky/RSS_reader',
    package_dir={
        '': 'RSS_reader',
    },
    packages=find_packages(where='RSS_reader'),
    entry_points={
        'console_scripts': ['rss-reader=command_line: main'],
    },
    python_requires='>=3.7',
    install_requires=[
        'feedparser',
        'bs4',
    ],
    long_description="RSS_reader",
    include_package_data=True
)
