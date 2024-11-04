menu = ''' Seja Bem vindo ao Banco C6

Digite a opção desejada:

Digite [d] para Depósito:

Digite [s] para Saque:

Digite [e] para Extrato:

    Aperte [x] para sair
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:


    opcao = input(menu)

    if opcao.lower() == 'd':
        
        deposito_string = input('Digite o valor a ser depositado ')
        valor_deposito =float(deposito_string)
        if valor_deposito < 1:
             print("Deposite o valor positivo")     
        else:
             saldo = saldo + valor_deposito
             extrato = extrato +  f"Depósito efetuado de R${valor_deposito:.2f} \n"
             print("Operação bem sucedida \n")       
             
    elif opcao.lower() == 's':
            saque_string = input('Digite o valor a ser sacado ')
            valor_saque= int(saque_string)
            if valor_saque > 500:
                    print("Seu limite é de R$500,00 por saque. \n")
            else:        
                if numero_saques >= LIMITE_SAQUES:
                    print("Limite de Saques diários atigindo. \n")  

                else:
                    if saldo >= valor_saque:
                        saldo = saldo - valor_saque
                        extrato = extrato +  f"Saque efetuado no valor de R${valor_saque:.2f} \n"
                        numero_saques = numero_saques + 1
                        print("Operação bem sucedida! \n")
                    else:
                        print("Saldo Insuficiente.")     

    elif opcao.lower() == 'e':
        if extrato =='':
            print("Não foram realizadas movimentações.") 
        else:
           print(extrato)  
           print(f"Saldo total na conta corrente R${saldo:.2f}")     

    elif opcao.lower() == 'x':
        break            
    
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.') 

   