try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="junkfile",
    version="1.0.0",
    description="Directory organizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ivan José Frezza Júnior",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    keywords="python organize project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    #install_requires=["Pyside2", "pyqt", "qt"],
    python_requires="~=3.6"
)
