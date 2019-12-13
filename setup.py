from setuptools import setup
from setuptools import find_packages

setup(
    name='rss_reader',
    version='1.0',
    description='RSS reader',
    author='Anton Stychnesky',
    author_email='stychnevsky@gmail.com',
    url='https://github.com/Stychnevsky/RSS_reader',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['rss-reader=rss_reader.rss_reader:rss_reader'],
    },
    python_requires='>=3.7',
    install_requires=[
        'feedparser',
        'bs4',
    ],
    long_description="RSS_reader",
    include_package_data=True
)