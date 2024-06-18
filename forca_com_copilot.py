def read_word_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            word = file.readline().strip()
            return word
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado.")
        return None

def display_hangman(remaining_attempts):
    stages = [
        
        """
          _________
         |/        |
         |         O
         |        \|/
         |        / \\
         |
        _|___
        """,
        # 1: cabeça, tronco, dois braços e uma perna
        """
          _________
         |/        |
         |         O
         |        \|/
         |        / 
         |
        _|___
        """,
        # 2: cabeça, tronco e dois braços
        """
          _________
         |/        |
         |         O
         |        \|/
         |        
         |
        _|___
        """,
        # 3: cabeça, tronco e um braço
        """
          _________
         |/        |
         |         O
         |        \|
         |        
         |
        _|___
        """,
        # 4: cabeça e tronco
        """
          _________
         |/        |
         |         O
         |         |
         |        
         |
        _|___
        """,
        # 5: cabeça
        """
          _________
         |/        |
         |         O
         |        
         |        
         |
        _|___
        """,
        # 6: estrutura inicial
        """
          _________
         |/        |
         |         
         |        
         |        
         |
        _|___
        """
    ]
    print(stages[remaining_attempts])

def display_progress(secret_word, guessed_letters):
    progress = ''
    for letter in secret_word:
        if letter in guessed_letters:
            progress += letter
        else:
            progress += '_'
    print("Progresso:", progress)

def guess_letter(secret_word, guessed_letters):
    letter = input("Insira uma letra: ").lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            print("Você já adivinhou essa letra.")
        else:
            guessed_letters.append(letter)
            if letter in secret_word:
                print("Letra correta!")
            else:
                print("Letra errada!")
    else:
        print("Entrada inválida. Por favor, insira apenas uma letra do alfabeto.")
    return guessed_letters

def play_game(secret_word):
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nTentativas restantes:", attempts)
        display_hangman(attempts)
        display_progress(secret_word, guessed_letters)
        guessed_letters = guess_letter(secret_word, guessed_letters)

        if set(secret_word) <= set(guessed_letters):
            print("Parabéns! Você adivinhou a palavra secreta:", secret_word)
            return

        if guessed_letters and guessed_letters[-1] not in secret_word:
            attempts -= 1

    print("Você perdeu! A palavra secreta era:", secret_word)

# Exemplo de uso:
file_path = 'word.txt'
secret_word = read_word_from_file(file_path)
if secret_word:
    play_game(secret_word)
