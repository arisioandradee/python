import importlib

import Aula33_m

print(Aula33_m.variavel)

for i in range(10):
    importlib.reload(Aula33_m)
    print(i)

print('Fim')