#
#
#
# Aritméticos:
#
#
#

#adição
print(1+2)

#subtração
print(2-3)

#multiplicação
print(3*4)

#divisão
print(4/5)

#divisão inteira
print(5//6)

#módulo
print(6%7)

#exponenciação
print(7**8)

#precedencia de operadores
#10 ou 0?
print(10-5*2)
print((10-5)*2)

print(10**2 * 2)
print(10**(2 * 2))


#
#
#
# de comparação
print("Comparação:   ")
#
#
#
print(50 == 50)
print(50 == 51)
print(50 < 51)
print(50 > 51)
print(50 <= 51)
print(50 >= 51)
print(50 <= 50)
print(50 >= 50)



#
#
#
# de atribuição
print("Atribuição:   ")
#
#
#

saldo = 500
print(saldo)

saldo+=200
print(saldo)

saldo-=200
print(saldo)

saldo*=200
print(saldo)

saldo/=200
print(saldo)

saldo//=200
print(saldo)

saldo = 500
saldo%=200
print(saldo)

saldo**=200
print(saldo)



#
#
#
# Lógicos
print("Lógicos:   ")
#
#
#

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
print(saque <= limite)

print(saldo >= saque and saque <= limite)

print(saldo >= saque or saque <= limite)

print(saldo >= saque and not saque <= limite)


print(not [])
print(not "")
print(not (True and False))
print(True or False)


#
#
#
#
#de identidade
print("de identidade")
#
#
#
#
curso = "curso"
nome_curso = curso
saldo, limite = "200", "200" 

print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)


#a = input("a: ")
#b = input("b: ")

#print(a is b)
#>> False





#
#
#
#
#de associação
print("de Associação")
#
#
#
#

texto = "era uma vez um pudim"
items = ["item 1", 'item 2', "item 3"]
saques = [1000, 2000]

print("pudim" in texto)
print("pudins" in texto)

print("item 2" in items)
print("maçã" in items)

print(1000 in saques)
