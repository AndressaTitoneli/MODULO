# cada arquivo tem sua caracteristicas
# pra cada modulo, adicionar arquivos pertinentes ao mesmo.

# AULA 83. Importando um modulo.
# importar com import
# importar com from 
'''
import funcoes

funcoes.somar()
funcoes.multi()

'''

'''
from funcoes import somar, multi

somar()
multi()

'''
# AULA 84. Criando e Importando Packages 
'''
from funcoes import somar
from funcoes import multi
from items.cadastro import cliente

somar()
multi()
cliente()
'''
# AULA 85. Aplicando um modulo
'''
from funcoes import find_index

list1 = ['a', 'b', 'c', 'd', 'e']

var1 = find_index(list1, 'e')
print(var1)
'''

# AULA 86. Desafios/explicando como funciona.

# AULA 87. If Else - Ponto do Steak 