# Nomes:
# João Paulo Dantas Lobo
# Larissa Antoniazzi




import csv
import pandas as pd

class TodoTarefa:
    def __init__(self,nome_arquivo = 'lista_tarefas.csv',nome='nome',categoria='categoria',data = 'data',status = 'status'):
        self.nome_arquivo = nome_arquivo
        conteudo = [nome,categoria,data,status]
        lista_arquivos = os.listdir()
        if nome_arquivo in lista_arquivos:
            with open(nome_arquivo,'w') as arquivo:
                escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
                escritor.writerow(conteudo) 
        else:
            with open(nome_arquivo,'a') as arquivo:
                escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
                escritor.writerow(conteudo) 

    def adicionar_tarefa(self,nome,categoria,data,status = 'Pendente'):
        conteudo = [nome,categoria,data,status]
        with open(self.nome_arquivo,'a') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerow(conteudo)

    def visualizar_tarefas(self, data = 'Hoje'):
        tarefas = pd.read_csv(self.nome_arquivo,delimiter=';')
        print(tarefas[tarefas.data == data])
    
    def alterar_status(self, tarefa):
        with open(self.nome_arquivo) as arquivo:
            lista_tarefas = list(csv.reader(arquivo, delimiter = ';', lineterminator = '\n'))
            for linha in lista_tarefas:
                if tarefa in linha and linha[3] == 'Pendente':
                    linha[3] = 'Concluido'
                elif tarefa in linha and linha[3] == 'Concluido':
                    linha[3] = 'Pendente'
        with open(self.nome_arquivo,'w') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerows(lista_tarefas) 

    def remover_tarefa(self, tarefa):
        with open(self.nome_arquivo) as arquivo:
            lista_tarefas = list(csv.reader(arquivo, delimiter = ';', lineterminator = '\n'))
            for linha in lista_tarefas:
                if tarefa in linha:
                    lista_tarefas.remove(linha)
        with open(self.nome_arquivo,'w') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerows(lista_tarefas) 

    def sair():
        break