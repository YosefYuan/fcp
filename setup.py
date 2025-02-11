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
    author="Your Name",
    description="A CLI tool to format input strings and copy to clipboard.",
    url="https://github.com/yourname/fcp-tool",  # 你的GitHub仓库（可选）
)
