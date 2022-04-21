# O que será verificado:

# 2.1 - Retorne True se a palavra passada por
# parâmetro for um palíndromo

# 2.2 - Retorne False se a palavra passada por
# parâmetro não for um palíndromo

# 2.3 - Retorne False se nenhuma palavra for
# passada por parâmetro

def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif low_index >= high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
