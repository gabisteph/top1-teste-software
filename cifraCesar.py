'''
Aluna: Gabrielle Stephanie Pires Mestrinho
Matrícula: 1715080565
Disciplina: Tópicos especiais para computação I

'''
# Função para criptografar a String input
def critografar_nome(nome, deslocamento ):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nome_criptografado = ""

    for i in range(len(nome)):
        posicao = alfabeto.find(nome[i])
        nome_criptografado += alfabeto[(posicao - deslocamento) % len(alfabeto)]

    return nome_criptografado
# Função para retornar e validar a quatidade de casos de teste
def caso_teste():
    qtd_casos_teste = input("Número de casos: ")
    while not qtd_casos_teste.isnumeric():
        qtd_casos_teste = input("O número de casos deve ser um número inteiro\nReescreva: ")
    qtd_casos_teste = int(qtd_casos_teste)
    return qtd_casos_teste
# Função para retorna e validar nome inserido pelo usuário
def nome_para_criptografar():
    # nome = input().upper()
    nome = input("Escreva a sentença: ").upper()
    while not nome.isalpha():
        nome = input("A sentença deve possuir apenas letras\nReescreva: ").upper()
    while len(nome) > 50:
        nome = input("A sentença deve possuir no máximo 50 caracteres\nReescreva: ").upper()
    return nome
# Função para retorna e validar o deslocamento
def deslocamento():
    # deslocamento = input()
    deslocamento = input("deslocamento: ")
    while not deslocamento.isdigit() or not ( 0 <= int(deslocamento) <= 25):
        deslocamento = input("O deslocamento deve ser um número inteiro de 0 a 25.\nReescreva novamente o deslocamento: ")
    return int(deslocamento)
# Função que executa a criptografia que usuário input
def cifra_Cesar():
    qtd_casos_teste = caso_teste()
    nomes_criptografados = []
    for _ in range(qtd_casos_teste):
        nome = nome_para_criptografar()
        deslocamento_val = deslocamento()

        criptograda = critografar_nome(nome, deslocamento_val)
        nomes_criptografados.append(criptograda)
    return nomes_criptografados
# execução principal
if __name__ == '__main__':
    cifra_Cesar()

