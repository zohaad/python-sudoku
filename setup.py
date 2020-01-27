from setuptools import find_packages, setup

setup(
    name="sudoku",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["sudoku = sudoku.__main__:main"]
    },
    install_requires=["attrs",],
    tests_require=["pytest"],
)
