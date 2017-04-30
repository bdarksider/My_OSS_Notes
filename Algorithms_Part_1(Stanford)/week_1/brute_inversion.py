# complexity
def calc_inversions(array):
    inversions = 0
    for i in range(len(array)):
        compare_from = array[i]
        for j in range(i, len(array)):
            compare_to = array[j]
            if compare_from > compare_to:
                inversions += 1
    return inversions

print(calc_inversions([1,2,3,4,5,6]))
print(calc_inversions([1,3,5,2,4,6]))
print(calc_inversions([6,5,4,3,2,1]))
