#São eles: not, and, or.

n1 = 10
n2 = 20
n3 = 30

print(not n2 > n1) #Era true, porém o not inverteu para false.
print(not n2 < n1)

print(n3 > n1 and n3 > n2) #True, pois n3 é maior que n1 e n2

print(n2 > n3 or n2 > n1) #True, pois apenas uma comparação precisa ser verdade, e n2 é maior que n1