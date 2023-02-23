def sacar(valor:float ): 
    saldo = 500
    if saldo >= valor:
        saldo -= valor
        print('Saque Efetuado')
    else:
        print("saque não efetuado")




sacar(150)
    