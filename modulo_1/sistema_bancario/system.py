data = {
    'saldo':0.0,
    'opcode':0,
    'saques':0,
    'extrato':''
}


def depositar(valor):
    if valor > 0:
        print("Depósito realizado com sucesso")
        data['saldo']    += valor
        data['extrato'] += f"{data['opcode']}. Depósito no valor de R$ {valor:.2f}\n"
        data['opcode']   += 1
    else:
        print('valor inválido')

def sacar(valor):
    if valor <= data['saldo'] and data['saques'] < 3 and valor <= 500:
        print("Saque realizado com sucesso")
        data['saldo']    -= valor
        data['extrato'] += f"{data['opcode']}. Saque no valor de R$ {valor:.2f}\n"
        data['opcode']   += 1
        data['saques']   += 1
    elif valor > data['saldo']: 
        print('Não é possível completar a operação por falta de saldo na conta')
    elif valor > 500:
        print("Valor Inválido")
    else:
        print("Limite de saques atingido")
        
def extrato():
    if data['extrato']:
        print(data['extrato'])
    else:
        print('Não foram Realizadas movimentações.')

def operation():
    while True:
        menusaldo = (f"saldo: {data['saldo']:.2f}").center(33) 
        menu = f"""
================ MENU ================
{menusaldo}

    Operações:

    1. Depósito
    2. Saque
    3. Extrato
    4. Sair

======================================
Digite o número da operação desejada
> """
        operation = input(menu)
        if operation == '1':
            depositar(float(input("Digite o valor: ")))
        elif operation == '2':
            sacar(float(input("Digite o valor: ")))
        elif operation == '3':
            extrato()
        elif operation == '4':
            break
        else:
            print('Operação inválida')
operation()