from setuptools import setup, find_packages

# try:
#    from pip._internal.req import parse_requirements
# except ImportError:
#    from pip.req import parse_requirements

setup(
    name='rss_reader',
    version='1.0',
    description='RSS reader',
    author='Anton Stychnesky',
    author_email='stychnevsky@gmail.com',
    url='https://github.com/Stychnevsky/RSS_reader',
    packages=find_packages(),
    # data_files=[('rss_reader', ['rss_reader/Arial-Unicode-Regular.ttf'])],
    entry_points={
        'console_scripts': ['rss-reader=rss_reader.rss_reader:main'],
    },
    python_requires='>=3.7',
       install_requires=[
           'feedparser',
           'argparse',
           'beautifulsoup4',


       ],
    long_description="RSS_reader",
    include_package_data=True
)
