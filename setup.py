from setuptools import find_packages, setup

setup(
    name='htmlDiscordTranscript',
    packages=find_packages(include=['htmlDiscordTranscript']),
    version='0.1.1',
    description='A library to create HTML files from discord channels',
    author='Kaiy',
    install_requires=['discord.py'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)