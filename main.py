## --- External modules imports --- ##

## --- Internal modules imports --- ##


saldo = 0
operacoes_restantes = 3
maximo_saque = 500
saques = 0
soma_saques = 0
depositos = 0
soma_depositos = 0
sep = '======================================'

while(True):

    tecla = input("Digite a operação desejada\r\n>>")

    print(f"\r\n{sep}")

    if tecla == 'e':
        
        print("Operação de extrato escolhida")
        print("Detalhes da sua conta:")
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Depositos realizados Hoje: {depositos}")
        print(f"Valor depositado Hoje: R$ {soma_depositos:.2f}")
        print(f"Saques realizados Hoje: {saques}")
        print(f"Valor retirado Hoje: R$ {soma_saques:.2f}")

    elif tecla == 'd':

        print("Operação de deposito escolhida")

        try:
            valor = float(input("Digite o valor positivo para deposito\r\n>>"))
            if valor > 0:
                saldo += valor
                depositos += 1
                soma_depositos += valor
                print("Operação de deposito realizada com sucesso")

            else:
                print("Valor escolhido é inválido.")

        except Exception as e:
            print("Valor escolhido deve ser numérico")

    elif tecla == 's':

        print("Operação de saque escolhida")

        try:
            valor = float(input("Digite o valor para sacar\r\n>>"))
            if valor > 0:

                if (valor <= maximo_saque):

                    if valor <= saldo:
                        saldo -= valor
                        saques += 1
                        soma_saques += valor
                        print("Operação de saque realizada com sucesso")

                    else:
                        print(f"Valor escolhido maior que o saldo atual da conta")

                else:
                    print(f"Valor maximo de saque é de R$ {maximo_saque:.2f}")

            else:
                print("Valor escolhido é inválido.")

        except Exception as e:
            print("Valor escolhido deve ser numérico")

    elif tecla == 'q':
        print("Fechando aplicação do banco...")
        break

    else:
        print("Operação invalida.")
        continue

    print(f"{sep}\r\n")


