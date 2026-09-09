import os
import subprocess

logo = r""" __  __                        ____          _      _ 
|  \/  | ___  _ __ ___  ___   / ___|___   __| | ___| |
| |\/| |/ _ \| '__/ __|/ _ \ | |   / _ \ / _` |/ _ \ |
| |  | | (_) | |  \__ \  __/ | |__| (_) | (_| |  __/_|
|_|  |_|\___/|_|  |___/\___|  \____\___/ \__,_|\___(_)"""

MORSE_ALPHABET = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..'
}

MORSE_NUMBERS = {
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

MORSE_SYMBOLS = {
    '.': '.-.-.-',   ',': '--..--',   '?': '..--..',
    '=': '-...-',    '/': '-..-.',    '@': '.--.-.',
    '!': '-.-.--',   '+': '.-.-.',    '-': '-....-'
}

TEXT_TO_MORSE = {**MORSE_ALPHABET, **MORSE_NUMBERS, **MORSE_SYMBOLS}
MORSE_TO_TEXT = {value: key for (key, value) in TEXT_TO_MORSE.items()}
WORD_DEL = '|'


def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def clean_text(text):
    return ' '.join(text.split())


def to_morse(message):
    output = []
    for char in message.upper():
        if char == ' ':
            output.append(WORD_DEL)
        else:
            output.append(TEXT_TO_MORSE.get(char, char))

    morse_msg = ' '.join(output)
    morse_msg = clean_text(morse_msg)
    return morse_msg


def to_text(code):
    output = []
    for letter in code.split():
        if letter == WORD_DEL:
            output.append(letter)
        else:
            output.append(MORSE_TO_TEXT.get(letter, ""))

    txt_msg = ''.join(' ' if letter == WORD_DEL else letter for letter in output)
    txt_msg = clean_text(txt_msg)
    return txt_msg.strip()


print(logo)
print("Welcome to Morse Code Machine!")
program_on = True
while program_on:
    try:
        answer = int(input("1. Text Message to Morse code\n"
                        "2. Morse Code to Text Message\n"
                        "Choose a number: "))
    except ValueError:
        clear()
        print("WARNING: Invalid input! Please enter 1 or 2.")
        continue

    if answer == 1:
        text_message = input("Please enter text message:\n")
        cleaned_text = clean_text(text_message)
        clear()
        print(f"Here is your message in morse code:\n{to_morse(cleaned_text)}\n")

    elif answer == 2:
        morse_message = input("Please enter morse message, use space between letters and '|' between words:\n")
        cleaned_morse = clean_text(morse_message)
        clear()
        print(f"Here is the morse code translated to text:\n{to_text(cleaned_morse)}\n")

    else:
        print("Bye Bye!")
        program_on = False
