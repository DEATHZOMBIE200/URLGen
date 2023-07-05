import random
import string
import pyperclip
import time
import webbrowser

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    max_iterations = 10
    for iteration in range(1, max_iterations + 1):
        random_string = generate_random_string(6).lower()
        url = "https://prnt.sc/" + random_string
        pyperclip.copy(url)
        print("Random URL copied to clipboard:", url)
        webbrowser.open_new_tab(url)
        time.sleep(0.1)  # Wait for 1 second before the next iteration

if __name__ == "__main__":
    main()
