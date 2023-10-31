from setuptools import setup
def readme():
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='funniest',
    version='0.1',
    packages=["src"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gptline = src.main:main"
        ]
    },
)
