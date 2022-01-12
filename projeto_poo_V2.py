
import csv
import pandas as pd
import os 


def verifica_arquivo(nome_arquivo, nome='nome',categoria='categoria',data = 'data',status = 'status'):
        conteudo = [nome,categoria,data,status]
        lista_arquivos = os.listdir()
        if nome_arquivo in lista_arquivos:
            while True:
                arquivo_existente = input(f'''Esse arquivo já existe, deseja:   
                                        1 . Sobrescresver?
                                        2 . Alterar?
                                        3 . Criar um arquivo com um novo nome? 
                ''')

                if arquivo_existente == '1':
                    with open(nome_arquivo,'w') as arquivo:
                        escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
                        escritor.writerow(conteudo)
                    return(nome_arquivo)

                elif arquivo_existente == '2':
                    return(nome_arquivo)

                elif arquivo_existente == '3':
                    nome_arquivo = input('Digite o nome da lista de tarefas que voce quer alterar ou criar uma nova caso não exista: (Não esqueça do .csv no final) \n')
                    nome_arquivo = verifica_arquivo(nome_arquivo = nome_arquivo)
                    return(nome_arquivo)

                else:
                    print('Digitou opção errada.')
        else:
            with open(nome_arquivo,'w') as arquivo:
                escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
                escritor.writerow(conteudo)
            return(nome_arquivo)




class TodoTarefa:

    def __init__(self,nome_arquivo = 'lista_tarefas.csv'):
        self.nome_arquivo = verifica_arquivo(nome_arquivo = nome_arquivo)
                    
    def adicionar_tarefa(self,tarefa,categoria,data,status = 'Pendente'):
        conteudo = [tarefa,categoria,data,status]
        with open(self.nome_arquivo,'a') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerow(conteudo)

    def visualizar_tarefas(self, data):
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
         



def main():
    nome_lista = input('Digite o nome da lista de tarefas que voce quer alterar ou criar uma nova caso não exista: (Não esqueça do .csv no final) \n')
    lista_tarefas = TodoTarefa(nome_arquivo = nome_lista)
    while True:
        escolha_opcao = input(f'''Digite:
                                1 . Adicionar uma nova tarefa.
                                2 . Visualizar tarefas.
                                3 . Remover uma tarefa.
                                4 . Alterar status da tarefa.
                                5 . Finalizar o programa.
        ''')
        if escolha_opcao == '1':
            tarefa = input('Digite o nome da tarefa: \n')
            categoria = input('Digite a categoria da tarefa: \n')
            data = input('Digite a data da tarefa (dd/mm/aaaa): \n')
            lista_tarefas.adicionar_tarefa(tarefa = tarefa, categoria= categoria, data = data)
        elif escolha_opcao == '2':
            data = input('Digite a data das tarefas que quer visualizar (dd/mm/aaaa):  \n')
            lista_tarefas.visualizar_tarefas(data = data)
        elif escolha_opcao == '3':
            tarefa = input('Digite o nome da tarefa que você quer remover: \n')
            lista_tarefas.remover_tarefa(tarefa = tarefa)
        elif escolha_opcao == '4':
            tarefa = input('Digite o nome da tarefa que voce quer alterar o status: \n')
            lista_tarefas.alterar_status(tarefa = tarefa)
        elif escolha_opcao == '5':
            break


main ()