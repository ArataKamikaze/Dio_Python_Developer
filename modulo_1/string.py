x = "   palavras exemplo  "

print(x.strip(),end="#\n")
print(x.lstrip(),end="#\n")
print(x.rstrip(),end="#\n")

name = "     LuCaS "
print(name.strip().title().center(15,'-'))


#invert string
name ='Sharknado henrique da silva'
print(name[::-1])


#string tripla
name = '''
olá meu nome é arata
espero que isso funcione
eu gosto de pudim
'''

print(name)