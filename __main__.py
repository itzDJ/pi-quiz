"""
Quiz to test your knowledge of the first 314 digits of pi.

Source for detecting user input without pressing enter:
https://www.codegrepper.com/code-examples/python/how+to+take+input+from+user+in+python+without+pressing+enter
"""

from pathlib import Path
import sys
import tty


def print_digits() -> None:
    # Print digits of pi from pi.txt adding a space every five digits
    print("")

    print("π =\n3.")
    with open(f"{file_dir}/pi.txt") as f:
        for text in f:
            digit = 0
            # text[2:] removes the first two characters of the string: "3."
            for char in text[2:]:
                print(char, end="")
                digit += 1
                if digit == 5:
                    print("")
                    digit = 0

    print("\n")


def quiz() -> None:
    print("\nWelcome to DJ's Pi Quiz!")
    print("cHeAt: Press '-' to skip a digit.")
    print("π = ", end="", flush=True)
    tty.setcbreak(sys.stdin)

    with open(f"{file_dir}/pi.txt") as f:
        pi = f.read()

        for index, digit in enumerate(pi):
            char = sys.stdin.read(1)[0]

            if char == digit:
                # Print the character in green.
                print(f"\033[32m{char}\033[0m", end="", flush=True)
            elif char == "-":
                # Print the correct character.
                print(digit, end="", flush=True)
            else:
                # Print the character in red.
                print(f"\033[31m{char}\033[0m")

                # Print which digit the user pressed wrong.
                if index == 0:
                    print("You messed up on digit 1.")
                elif index == 1:
                    print("You forgot the decimal place.")
                else:
                    print(f"You messed up on digit {index}.")

                # End the loop ending the quiz.
                break
    print("")


if __name__ == "__main__":
    # Get the directory of the folder: pi_quiz
    file_dir = Path(__file__).absolute().parent

    usage = "\nUsage:\n  python3 pi_quiz --digits\n  python3 pi_quiz --quiz\n"
    try:
        args = sys.argv[1]
    except IndexError:
        print(usage)
        sys.exit()

    if args == "--digits":
        print_digits()
    elif args == "--quiz":
        quiz()
    else:
        print(usage)

