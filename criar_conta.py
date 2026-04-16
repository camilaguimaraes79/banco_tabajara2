from Cliente import Cliente 
import pandas as pd
class Criar_Conta:
    def __init__(self , nome_cliente,cpf,tipo_conta):  
        

        numero_conta = 0
        agencia = 400
        extrato_bancario = 0
        
        self.cliente = Cliente(nome_cliente, cpf, tipo_conta)
        
    def salvar_excel(self , caminho_excel):

        dados_cliente = self.cliente.dicionario_cliente()

        excel = pd.DataFrame(dados_cliente)
        return excel 
