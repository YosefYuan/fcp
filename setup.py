from setuptools import setup, find_packages

setup(
    name="fcp-tool",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pyperclip",
        "inquirer"
    ],
    entry_points={
        "console_scripts": [
            "fcp=fcp.main:cli"
        ]
    },
    author="Joseph Yuan",
    description="A CLI tool to format input strings and copy to clipboard.",
    url="https://github.com/YosefYuan/fcp"
)
