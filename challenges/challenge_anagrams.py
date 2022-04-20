# O que será verificado:

# 3.1 - Retorne True se as palavras passadas forem anagramas

# 3.2 - Retorne False se as palavras passadas por parâmetro não forem anagramas

# 3.3 - Retorne False se alguma das palavras passadas por parâmetro for uma string vazia

# 3.4 - Execute a função, somando 10.000 execuções para uma entrada pequena, em menos que 8.2s (tempo da execução do avaliador no Pull Request)

# 3.5 - Retorne True se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas

def insertion_sort_ordenation(string):
    list_string = []
    list_string[:0]=string

    for i in range(len(list_string)):
        current_value = list_string[i]
        position = i
        while position > 0 and list_string[position - 1] > current_value:
            list_string[position] = list_string[position - 1]
            position -= 1
        list_string[position] = current_value
    return list_string


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    else:
        if insertion_sort_ordenation(first_string) == insertion_sort_ordenation(second_string):
            return True
        else:
            return False


