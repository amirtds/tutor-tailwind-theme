import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tailwind_theme", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-tailwind-theme",
    version=ABOUT["__version__"],
    url="https://github.com/amirtds/tutor-tailwind-theme",
    project_urls={
        "Code": "https://github.com/amirtds/tutor-tailwind-theme",
        "Issue tracker": "https://github.com/amirtds/tutor-tailwind-theme/issues",
    },
    license="Not open source",
    author="Amir Tadrisi",
    author_email="amirtds@gmail.com",
    description="Tutor theme powered by TailwindCSS",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor>=18.0.0,<19.0.0"],
    extras_require={
        "dev": [
            "tutor[dev]>=18.0.0,<19.0.0",
        ]
    },
    entry_points={
        "tutor.plugin.v1": [
            "tailwind-theme = tailwind_theme.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
