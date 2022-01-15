import csv
import pandas as pd
import os 
import inquirer
import datetime as dt
from time import sleep


def verifica_arquivo(nome_arquivo, nome='nome',categoria='categoria',data = 'data',status = 'status'):

    print('\n')
    conteudo = [nome,categoria,data,status]
    lista_arquivos = os.listdir()
    perguntas = ['Sobrescresver?','Alterar?','Criar um arquivo com um novo nome?']
    if nome_arquivo in lista_arquivos:
        while True:
            pergunta = [
                inquirer.List('option',
                message='Esse arquivo já existe, deseja:',
                choices=[
                    perguntas[0],
                    perguntas[1],
                    perguntas[2]
                        ])]

            arquivo_existente = inquirer.prompt(pergunta)
            sleep(1)
                
            if arquivo_existente['option'] == perguntas[0]:
                with open(nome_arquivo,'w') as arquivo:
                    escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
                    escritor.writerow(conteudo)
                return(nome_arquivo)

            elif arquivo_existente['option'] == perguntas[1]:
                return(nome_arquivo)

            elif arquivo_existente['option'] == perguntas[2]:
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

    def visualizar_todas_tarefas(self):
        tarefas = pd.read_csv(self.nome_arquivo,delimiter=';')
        print(tarefas)
    
    def alterar_status(self, tarefa):
        hoje = dt.date.today().strftime('%d/%m/%Y')
        amanha = (dt.date.today() + dt.timedelta(days = 1)).strftime('%d/%m/%Y') 

        with open(self.nome_arquivo) as arquivo:
            lista_tarefas = list(csv.reader(arquivo, delimiter = ';', lineterminator = '\n'))
            lista_nome_tarefas = [linha[0] for linha in lista_tarefas]
            qtd_mesma_tarefa = lista_nome_tarefas.count(tarefa)

            if qtd_mesma_tarefa == 1:
                for linha in lista_tarefas:
                    if tarefa in linha and linha[3] == 'Pendente':
                        linha[3] = 'Concluido'
                    elif tarefa in linha and linha[3] == 'Concluido':
                        linha[3] = 'Pendente'

            elif qtd_mesma_tarefa > 1:
                pergunta_data = [
                    inquirer.List('data',
                    message= f'''Existem {qtd_mesma_tarefa} de tarefas com o mesmo nome, qual a data da tarefa que você quer alterar o status?''',
                    choices=[
                        'Hoje',
                        'Amanhã',
                        'Outro dia'
                            ])]
                data = inquirer.prompt(pergunta_data)

                sleep(1)

                if data['data'] == 'Hoje':
                    data = hoje
                    for linha in lista_tarefas:
                        if tarefa in linha and data in linha and linha[3] == 'Pendente' :
                            linha[3] = 'Concluido'
                        elif tarefa in linha and data in linha and linha[3] == 'Concluido':
                            linha[3] = 'Pendente'

                elif data['data'] == 'Amanhã':
                    data = amanha
                    for linha in lista_tarefas:
                        if tarefa in linha and data in linha and linha[3] == 'Pendente' :
                            linha[3] = 'Concluido'
                        elif tarefa in linha and data in linha and linha[3] == 'Concluido':
                            linha[3] = 'Pendente'

                else:
                    data = input('Digite a data da tarefa (dd/mm/aaaa): \n')
                    for linha in lista_tarefas:
                        if tarefa in linha and data in linha and linha[3] == 'Pendente' :
                            linha[3] = 'Concluido'
                        elif tarefa in linha and data in linha and linha[3] == 'Concluido':
                            linha[3] = 'Pendente'

        with open(self.nome_arquivo,'w') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerows(lista_tarefas) 

    def remover_tarefa(self, tarefa):
        hoje = dt.date.today().strftime('%d/%m/%Y')
        amanha = (dt.date.today() + dt.timedelta(days = 1)).strftime('%d/%m/%Y')  

        with open(self.nome_arquivo) as arquivo:
            lista_tarefas = list(csv.reader(arquivo, delimiter = ';', lineterminator = '\n'))
            lista_nome_tarefas = [linha[0] for linha in lista_tarefas]
            qtd_mesma_tarefa = lista_nome_tarefas.count(tarefa)

            if qtd_mesma_tarefa == 1:
                for linha in lista_tarefas:
                    if tarefa in linha:
                        lista_tarefas.remove(linha)

            elif qtd_mesma_tarefa > 1:
                pergunta_data = [
                    inquirer.List('data',
                    message= f'''Existem {qtd_mesma_tarefa} de tarefas com o mesmo nome, qual a data da tarefa que você quer remover?''',
                    choices=[
                        'Hoje',
                        'Amanhã',
                        'Outro dia'
                            ])]
                data = inquirer.prompt(pergunta_data)

                sleep(1)
                if data['data'] == 'Hoje':
                    data = hoje
                    for linha in lista_tarefas:
                        if tarefa in linha and data in linha:
                            lista_tarefas.remove(linha)
                
                elif data['data'] == 'Amanhã':
                    data = amanha
                    for linha in lista_tarefas:
                        if tarefa in linha and data in linha:
                            lista_tarefas.remove(linha)

                else:
                    data = input('Digite a data da tarefa (dd/mm/aaaa): \n')
                    for linha in lista_tarefas:
                        if tarefa in linha and data in linha:
                            lista_tarefas.remove(linha)

        with open(self.nome_arquivo,'w') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerows(lista_tarefas) 
         



def main():

    hoje = dt.date.today().strftime('%d/%m/%Y')
    amanha = (dt.date.today() + dt.timedelta(days = 1)).strftime('%d/%m/%Y')

    nome_lista = input('Digite o nome da lista de tarefas que voce quer alterar ou criar uma nova caso não exista: \n') + '.csv'
    lista_tarefas = TodoTarefa(nome_arquivo = nome_lista)
    perguntas =  ['Adicionar tarefa','Visualizar tarefas','Remover tarefa','Alterar status da tarefa','Encerrar']

    while True:


        pergunta = [
            inquirer.List('option',
            message='Escolha uma das opções abaixo',
            choices=[
                perguntas[0],
                perguntas[1],
                perguntas[2],
                perguntas[3],
                perguntas[4]
                    ])]

        resposta = inquirer.prompt(pergunta)

        sleep(1)

        if resposta['option'] == perguntas[0]:
            opcao_add_tarefa = [
            inquirer.Text('tarefa', message='Qual é o nome da tarefa?'),
            inquirer.Text('categoria', message='Qual é a categoria da tarefa?'),
            inquirer.List('data', message='Escolha a data da tarefa', choices = ['Hoje','Amanhã','Outra data'])
            ]

            resposta_add_tarefa = inquirer.prompt(opcao_add_tarefa)

            sleep(1)

            if resposta_add_tarefa['data'] == 'Hoje':
                lista_tarefas.adicionar_tarefa(tarefa = resposta_add_tarefa['tarefa'], categoria= resposta_add_tarefa['categoria'], data = hoje)
            elif resposta_add_tarefa['data'] == 'Amanhã':
                lista_tarefas.adicionar_tarefa(tarefa = resposta_add_tarefa['tarefa'], categoria= resposta_add_tarefa['categoria'], data = amanha)
            else:
                data = input('Digite a data da tarefa (dd/mm/aaaa): \n')
                print('\n')
                lista_tarefas.adicionar_tarefa(tarefa = resposta_add_tarefa['tarefa'], categoria= resposta_add_tarefa['categoria'], data = data)

        elif resposta['option'] == perguntas[1]:
            opcao_todas_tarefas = [
                inquirer.List('option',
                message='Quer vizualizar todas as tarefas da lista?',
                choices=[
                    'Sim',
                    'Não'
                ])]

            todas_tarefas = inquirer.prompt(opcao_todas_tarefas)

            sleep(1)

            if todas_tarefas['option'] == 'Sim':
                lista_tarefas.visualizar_todas_tarefas()
                print('\n')

            else:
                opcao_ver_tarefa = [
                    inquirer.List('data',
                    message='Quer ver as tarefas de qual dia?',
                    choices=[
                        'Hoje',
                        'Amanhã',
                        'Outro dia'
                    ])]

                resposta_ver_tarefa = inquirer.prompt(opcao_ver_tarefa)

                sleep(1)

                if resposta_ver_tarefa['data'] == 'Hoje':
                    lista_tarefas.visualizar_tarefas(data = hoje)
                    print('\n')
                elif resposta_ver_tarefa['data'] == 'Amanhã':
                    lista_tarefas.visualizar_tarefas(data = amanha)
                    print('\n')
                else:
                    data = input('Digite a data das tarefas que quer visualizar (dd/mm/aaaa):  \n')
                    lista_tarefas.visualizar_tarefas(data = data)
                    print('\n')

        elif resposta['option'] == perguntas[2]:
            tarefa = input('Digite o nome da tarefa que você quer remover: \n')
            lista_tarefas.remover_tarefa(tarefa = tarefa)
            
        elif resposta['option'] == perguntas[3]:
            tarefa = input('Digite o nome da tarefa que voce quer alterar o status: \n')
            lista_tarefas.alterar_status(tarefa = tarefa)
            
        else:
            os.system('cls')
            break
    

main ()