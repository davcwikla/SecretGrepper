import subprocess
import time

print("""\
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 
LinkedIn: https://www.linkedin.com/in/dcwikla/
Version: 1.0
Release date: 06.2023
""")

time.sleep(1)

print("----------------------------------------------------------------------------------------") 

time.sleep(1)

app_name = input("Wprowadź ścieżkę do pliku: ")

search_phrases_input = input("Wprowadź frazy do sprawdzenia, oddzielone przecinkami: ")
search_phrases = search_phrases_input.split(',')

def grep_in_strings(app_name, search_phrases):

    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    results = []
    
    for search_phrase in search_phrases:
        modified_search_phrase = search_phrase.strip() + "*"
        try:
            command = f"strings {app_name} | grep '{modified_search_phrase}'"
            result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
            if result.stdout:
                result_text = f"\nWynik dla frazy '{modified_search_phrase}'):\n" + \
                              f"---------------------------------\n{result.stdout.strip()}\n"
                print(f"{GREEN}{result_text}{RESET}")
                results.append(result_text)
            else:
                result_text = f"\nWynik dla frazy '{modified_search_phrase}':\n" + \
                              f"---------------------------------\nBrak wyników.\n"
                print(f"{RED}{result_text}{RESET}")
                results.append(result_text)
        except subprocess.CalledProcessError:
            result_text = f"\nWynik dla frazy '{modified_search_phrase}':\n" + \
                          f"---------------------------------\nNie znaleziono.\n"
            print(f"{RED}{result_text}{RESET}")
            results.append(result_text)
        if search_phrase != search_phrases[-1]: 
            response = input("\nCzy pokazać kolejny wynik? (Y/n): ").strip().lower()
            if response != 'y':
                print("Zakończono wyświetlanie wyników.")
                break

        time.sleep(1)
    
    save_results = input("\nCzy zapisać wyniki do pliku? (Y/n): ").strip().lower()
    if save_results == 'y':
        file_name = input("Podaj nazwę pliku do zapisu: ")
        with open(file_name, 'w') as file:
            file.writelines(results)
        print(f"Wyniki zostały zapisane do pliku {file_name}.")

def display_loading_bar(duration=3):
    print("Przetwarzanie...", end="")
    for i in range(duration):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")

display_loading_bar()

grep_in_strings(app_name, search_phrases)
