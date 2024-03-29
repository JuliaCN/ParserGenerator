from setuptools import setup, find_packages
from pathlib import Path


version = 0.1
with Path('README.md').open() as readme:
    readme = readme.read()


setup(
    name='pg',
    version=version if isinstance(version, str) else str(version),
    keywords="", # keywords of your project that separated by comma ","
    description="", # a concise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='bsd3',
    python_requires='>=3.10.0',
    url='https://github.com/JuliaCN/ParserGenerator',
    author='thautwarm, yeruoforever',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={"console_scripts": []},
    # above option specifies what commands to install,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd:compiler"]}
    install_requires=[], # dependencies
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)


