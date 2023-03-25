#!/usr/bin/env python
# -*- coding: utf-8 -*-   

'''
take a N number of letters and spin up the permutations and check which are words

'''

## ===================================================================
## LICENSE AND CREDITS
## This app/collection of scripts at https://github.com/mariochampion/liquibase-drift-reports
## released under the Apache License 2.0. (http://www.apache.org/licenses/LICENSE-2.0)
##
## Latest Liquibase Release: https://github.com/liquibase/liquibase/releases
## Contribute code to Liquibase: https://github.com/liquibase/liquibase
##
## please open issues and pull requests,
## thanks and always remember: this robot loves you. 
## boop boop!
## ===================================================================



################################# love your library(s)
import os, sys
import random

spanish_words = [ 'abogado', 'adiós', 'agencia', 'aireado', 'amantes', 'anuncio', 'arboles', 'ayuda', 'barroco', 'basquet', 'cajones', 'caminos', 'canela', 'canicas', 'chabola', 'cobalto', 'colegio', 'corrida', 'cuidado', 'cultivo', 'delfín', 'dolores', 'dorados', 'embuste', 'enfermo', 'estirpe', 'fábrica', 'farsante', 'futbol', 'gambito', 'gemelos', 'glotóns', 'guitar', 'hámster', 'hermoso', 'hielojo', 'inverno', 'jabalíe', 'jirafas', 'justos', 'kiriele', 'laderas', 'límites', 'lombriz', 'manitas', 'mártir', 'mazapán', 'minutos', 'moldura', 'nocturn',
]


def get_word(spanish_words):
    chosen_word = random.choice(spanish_words)
    chosen_word = chosen_word.lower()
    return chosen_word

def validate_letter(letter):
    if not letter.isalpha():
        print("Lo siento, eso no es una letra. Por favor, intenta de nuevo.")
        return False
    return True

def play_game():
    active_word = get_word(spanish_words)
    print("active word: " + active_word)
    print(" ")
    guessed_letters = set()
    max_guesses = 10
    
    while max_guesses > 0:
        print("Adivina una letra de la palabra de " + str(len(active_word)) + " letras:")
        print(" ".join([letter if letter in guessed_letters else "_" for letter in active_word]))
        print(" ")
        
        letter = raw_input("adivina una letra: ").lower()
        if not validate_letter(letter):
            continue
        
        if letter in guessed_letters:
            print("Ya adivinaste la letra '" + letter + "'. Por favor intenta otra.")
            continue
        
        guessed_letters.add(letter)
        if letter in active_word:
            positions = [i+1 for i, char in enumerate(active_word) if char == letter]
            print("La letra '" + letter + "' está en las palabra " + active_word + ".")
            if set(active_word) == guessed_letters:
                print(" ")
                print("-------!!!------------!!!---------")
                print("Felicidades! Adivinaste la palabra.")
                print("-------!!!------------!!!---------")
                print(" ")
                return
        else:
            max_guesses -= 1
            print("Lo siento, la letra '" + letter + "' no está en la palabra. Te quedan "+ str(max_guesses) + " intentos.")
    
    print("Lo siento, no adivinaste la palabra. La palabra era '" + active_word + "'.")



############## GET STARTED	

#################################
# boilerplate kicker offer (yes thats a tech term!)   
if __name__ == '__main__':
  
  play_game()


