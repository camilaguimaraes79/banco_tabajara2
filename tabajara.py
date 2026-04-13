from Cliente import Cliente 
from criar_conta import Criar_Conta
import pandas as pd
import os
caminho_excel = "cliente_banco_Tabajara.xlsx"

print("================================================")
print("                 BANCO TABAJARA")
print("                 Escolha uma opção")
print("                 1 - Criar conta")
print("                 2 - Acessar conta")
print("================================================\n")

opcao = int(input("R: "))

if opcao == 1:
    nome_cliente = str(input("Nome completo: "))
    cpf = int(input("CPF: "))
    tipo_conta = str(input("Tipo da conta que deseja criar: "))
    
    if os.path.exists(caminho_excel): #True
        print("Arquivo ja existe")
        df = pd.read_excel(caminho_excel)
        
    else: #false
        print('Arquivo não existe')
        
        df = pd.DataFrame()
        
        #Instancio para manipular  os dados adicionados pelo cliente 
        conta = Criar_Conta(nome_cliente, cpf, tipo_conta)
        
        #Identifico o caminho do excel e chamo a funcao salvar_excel
        novo_dado = conta.salvar_execel(caminho_excel)
        
        df = pd.concat([df, novo_dado], ignore_index=True)
        
    df.to_excel(caminho_excel, index=False)
elif opcao == 2:
    print("Opcao 2 selecionada")