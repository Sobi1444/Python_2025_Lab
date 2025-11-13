def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

def odwracanie_rek(L, left, right):
    if left >= right:
        return L
    L[left], L[right] = L[right], L[left]
    return odwracanie_rek(L, left+1, right-1)


L = [1, 2, 3, 4, 5, 6]
print (odwracanie_rek(L, 0, len(L) - 1))
print (odwracanie(L, 0, len(L) - 1))