from setuptools import setup, find_packages

setup(
    name='game',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here, e.g.,
        'pygame',
        # 'numpy',
    ],
    entry_points={
        'console_scripts': [
            'game = game.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/game',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
