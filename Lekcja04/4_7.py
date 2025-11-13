
def flatten(seq):
    lista = []
    for k in seq:
        if isinstance(k, (list, tuple)):
            for i in flatten(k):
                lista.append(i)
        else:
            lista.append(k)
    return lista




sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]