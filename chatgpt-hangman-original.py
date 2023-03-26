import random

def get_word():
    words = ['abogado', 'basquet', 'canela', 'dorados', 'enfermo', 'futbol', 'guitar']
    return random.choice(words)

def validate_letter(letter):
    if not letter.isalpha():
        print("Lo siento, eso no es una letra. Por favor, intenta de nuevo.")
        return False
    return True

def play_game():
    active_word = get_word()
    guessed_letters = set()
    max_guesses = 7
    
    while max_guesses > 0:
        print(f"Adivina una letra de la palabra de {len(active_word)} letras:")
        print(" ".join([letter if letter in guessed_letters else "_" for letter in active_word]))
        
        letter = input().lower()
        if not validate_letter(letter):
            continue
        
        if letter in guessed_letters:
            print(f"Ya adivinaste la letra '{letter}'. Por favor intenta otra.")
            continue
        
        guessed_letters.add(letter)
        if letter in active_word:
            positions = [i+1 for i, char in enumerate(active_word) if char == letter]
            print(f"La letra '{letter}' está en las posiciones {positions}.")
            if set(active_word) == guessed_letters:
                print("¡Felicidades! Adivinaste la palabra.")
                return
        else:
            max_guesses -= 1
            print(f"Lo siento, la letra '{letter}' no está en la palabra. Te quedan {max_guesses} intentos.")
    
    print(f"Lo siento, no adivinaste la palabra. La palabra era '{active_word}'.")

