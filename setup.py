from setuptools import setup, find_packages

setup(
    name='served',
    version='0.0.1',
    description='Python Discord bot for dedicated server hosting',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Carlton Bergeron',
    author_email='cjberger1993@outlook.com',
    url='https://served.gg',
    packages=find_packages(where='served'),
    python_requires='>=3.12',
    install_requires=[
        'discord.py>=2.0.0',
    ],
    classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
    ],
    license='MIT',
)