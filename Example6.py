def reverse(array):
    for i in range(len(array)//2):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
