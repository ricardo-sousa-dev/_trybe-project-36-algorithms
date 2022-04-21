# O que será verificado:

# 4.1 - Retorne o número repetivo se a função receber,
#  como parâmetro, uma lista com números repetidos

# 4.2 - Retorne False se a função não receber nenhum parâmetro

# 4.3 - Retorne False se a função receber, como parâmetro,
#  uma string

# 4.4 - Retorne False se a função receber, como parâmetro,
#  uma lista sem números repetidos

# 4.5 - Retorne False se a função receber, como parâmetro,
#  apenas um valor

# 4.6 - Retorne False se a função receber, como parâmetro,
#  um número negativo

# 4.7 - Execute a função, somando 10.000 execuções para uma
# entrada pequena, em menos que 0.01s (tempo da execução
# do avaliador no Pull Request)

def insertion_sort_ordenation(list_elements):
    for i in range(len(list_elements)):
        current_value = list_elements[i]
        position = i
        while position > 0 and list_elements[position - 1] > current_value:
            list_elements[position] = list_elements[position - 1]
            position -= 1
        list_elements[position] = current_value
    return list_elements


def binary_search_repeating_element(arr):
    # https://www.geeksforgeeks.org/find-repeating-element-sorted-array-size-n/
    low = 0
    high = len(arr) - 1

    if high < 1:
        raise Exception("Array is empty")

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] == arr[mid + 1]:
            return arr[mid]
        elif arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return arr[low]


# Driver code
arr = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
index = binary_search_repeating_element(arr)

if __name__ == '__main__':
    if (index != -1):
        print(arr[index])


def verify_type(nums):
    if not nums:
        return False
    if isinstance(nums, str):
        return False
    if len(nums) == 1:
        return False
    return True


def find_duplicate(nums):
    if not verify_type(nums):
        return False
    if len(nums) == 2:
        return nums[0] if nums[0] == nums[1] else False
    nums = insertion_sort_ordenation(nums)
    for i in range(len(nums)):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
    # if len(nums) > 2:
    #     nums = insertion_sort_ordenation(nums)
    #     return binary_search_repeating_element(nums)
