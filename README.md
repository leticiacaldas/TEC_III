Jogo da Forca

Este projeto implementa um jogo da forca em Python, onde os jogadores tentam adivinhar uma palavra secreta fornecida a partir de um arquivo de texto. O jogo foi desenvolvido como parte da disciplina optativa TECIII: Programação por Pares com IA na Universidade Federal de Pelotas, ministrada pela professora Patrícia A. Jaques Maillard.
Descrição

O jogo da forca é um clássico jogo de adivinhação de palavras. Os jogadores têm um número limitado de tentativas para adivinhar a palavra secreta, letra por letra. Cada tentativa incorreta resulta em uma parte do corpo do boneco da forca sendo desenhada. O jogo termina quando o jogador adivinha a palavra corretamente ou esgota todas as tentativas.
Funcionalidades

    Leitura da palavra secreta a partir de um arquivo de texto.
    Interface em linha de comando para interação com o jogador.
    Desenho do boneco da forca com base no número de tentativas restantes.
    Verificação e feedback de letras adivinhadas corretamente ou incorretamente.
    Exibição do progresso do jogador ao longo do jogo.

Estrutura do Código

    read_word_from_file(file_path): Lê a palavra secreta de um arquivo de texto.
    display_hangman(remaining_attempts): Exibe o estado atual do boneco da forca com base nas tentativas restantes.
    display_progress(secret_word, guessed_letters): Mostra o progresso do jogador, exibindo letras adivinhadas corretamente e espaços para as não adivinhadas.
    guess_letter(secret_word, guessed_letters): Recebe uma letra do jogador, verifica sua validade e atualiza a lista de letras adivinhadas.
    play_game(secret_word): Gerencia a lógica principal do jogo, incluindo o loop de tentativas e a verificação de vitória ou derrota.

   
Desenvolvimento

Este projeto foi desenvolvido com a assistência do GitHub Copilot, que forneceu sugestões de código e feedback em tempo real. O Copilot ajudou a acelerar o desenvolvimento, sugerindo trechos de código, corrigindo erros comuns e oferecendo melhorias para a estrutura do código.
Sobre a Disciplina

Este projeto faz parte da disciplina TECIII: Programação por Pares com IA na Universidade Federal de Pelotas, ministrada pela professora Patrícia A. Jaques Maillard. A disciplina explora técnicas de programação colaborativa e o uso de ferramentas de inteligência artificial para melhorar a produtividade e a qualidade do código.
Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Universidade Federal de Pelotas

Disciplina: TECIII: Programação por Pares com IA

Professora: Patrícia A. Jaques Maillard
