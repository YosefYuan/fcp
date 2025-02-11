import argparse
import pyperclip
import inquirer

def format_output(input_str, mode):
    if mode == "js":
        return input_str.replace("/", ".")
    elif mode == "css":
        return "--ds-" + input_str.replace("/", "-")

def main():
    parser = argparse.ArgumentParser(description="Format input string and copy to clipboard.")
    parser.add_argument("input", nargs="?", help="Input string (e.g., comp/typography/title/medium)")
    
    args = parser.parse_args()
    input_str = args.input if args.input else pyperclip.paste()
    
    questions = [
        inquirer.List(
            "mode",
            message="Choose output mode",
            choices=["js", "css"],
            default="js"
        )
    ]
    answers = inquirer.prompt(questions)
    mode = answers["mode"]
    
    result = format_output(input_str, mode)
    pyperclip.copy(result)
    print(f"Output ({mode}): {result} (Copied to clipboard)")

def cli():
    main()

if __name__ == "__main__":
    main()
