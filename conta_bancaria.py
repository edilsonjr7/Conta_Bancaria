class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.saques_diarios = 0
        self.limite_saques_diarios = 3  # Limite de 3 saques por dia

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Limite diário de saques atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_saque:
            print(f"Valor máximo para saque é de R$500.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    def mostrar_extrato(self):
        print("\n--- Extrato Bancário ---")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for item in self.extrato:
                print(item)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


# Programa principal
def main():
    conta = ContaBancaria()

    while True:
        print("\n--- MENU ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$"))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: R$"))
            conta.sacar(valor)
        elif opcao == '3':
            conta.mostrar_extrato()
        elif opcao == '4':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
