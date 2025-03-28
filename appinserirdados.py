import openpyxl
from openpyxl import Workbook
import os

def criar_ou_abrir_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
        wb = openpyxl.load_workbook(nome_arquivo)
        ws = wb.active
    else:
        wb = Workbook()
        ws = wb.active
        ws.append(["Dia Coleta", "Mês Coleta", "Ano Coleta", "Horário Coleta",
                   "Dia Nasc", "Mês Nasc", "Ano Nasc", "Horário Nasc",
                   "Procedimento Limpeza", "Peso (g)", "Altura (cm)", "Sexo",
                   "Semanas Gestação", "ID", "Nome Responsável",
                   "Whatsapp/Telefone", "Endereço", "Bairro"])
    return wb, ws

def inserir_dados(ws, dados):
    ws.append(dados)

def main():
    nome_arquivo = "trabalhocoleta.xlsx"
    wb, ws = criar_ou_abrir_arquivo(nome_arquivo)
    
    while True:
        print("\nInsira os dados do bebê:")
        dados = [
            input("Dia da coleta: "),
            input("Mês da coleta: "),
            input("Ano da coleta: "),
            input("Horário da coleta: "),
            input("Dia de nascimento: "),
            input("Mês de nascimento: "),
            input("Ano de nascimento: "),
            input("Horário de nascimento: "),
            input("Procedimento de limpeza: "),
            input("Peso (g): "),
            input("Altura (cm): "),
            input("Sexo: "),
            input("Semanas de gestação: "),
            input("ID: "),
            input("Nome do Pai/Mãe/Responsável: "),
            input("Whatsapp/Telefone: "),
            input("Endereço: "),
            input("Bairro: ")
        ]
        
        inserir_dados(ws, dados)
        wb.save(nome_arquivo)
        print("Dados salvos com sucesso!\n")
        
        continuar = input("Deseja inserir outro registro? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    wb.close()
    print("Encerrando o programa.")

if __name__ == "__main__":
    main()