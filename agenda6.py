# -*- coding: utf-8 -*-

#from datetime import date
#import sys
import time
#import os
import re



class Agenda():

    def __init__(self):
        self.lista = []
        self.contato = {
        }
        self.inicio()

    @property
    def DADOS_OUTPUT(self):
        self.gerar_id
        self.contato["ID"] = self.ID
        self.contato["nome"] = str(raw_input("Qual seu nome? \n"))
        self.contato["email"] = str(raw_input("Qual seu email? \n"))
        self.contato["telefone"] = str(raw_input("Qual seu contato? \n"))
        return {self, self.contato["ID"],self.contato["nome"],self.contato["email"], self.contato["telefone"]}

    @property
    def manipular_dados(self):
       return self.lista.append(self.contato)

    @property
    def gerar_id(self):
        ID = 0
        self.ID = ID + 1
        return (self.ID)

    @property
    def gerar_nome_arquivo(self):
        arquivo = raw_input("Digite o nome do seu arquivo.")
        formato = raw_input("Digite o formato. .txt ou .csv?")
        out = re.sub(r'[^\w\s+$]', '', arquivo)
        out2 = re.sub(r'[^\w\s+$]', '', formato)
        self.nome_arquivo = str("{}.{}".format(out, out2))
        return self

    def ler_arquivo(self):
        f = open("agenda.txt", 'r')
        lista = f.readlines.strip().split(",")
        print(lista)

    def criar_arquivo(self):
        self.gerar_nome_arquivo
        print("COMO FICOU O NOME DO ARQUIVO:")
        print(self.nome_arquivo)
        time.sleep(2)
        open(str(self.nome_arquivo), "a")
        print("ARQUIVO CRIADO!")






        self.start_agenda()

    def listar_contatos(self):
        if len(self.lista) > 0:
            for i, self.contato in enumerate(self.lista):
                print("\n")

                print("==============================================")
                print("contato {}:".format(i + 1))
                print("\tNome: {}".format(self.contato["nome"]))
                print("\tTelefone: {}".format(self.contato["telefone"]))
                print("\tEmail: {}".format(self.contato["email"]))
                print("==============================================")
                print("")

            print("Quantidade de contatos: {}\n".format(len(self.lista)))

        else:
            print("Não existe nenhum contato cadastrado para listar.\n")
        pass

    def salvar_contatos(self):
        self.manipular_dados
        arquivo = open("agenda.txt", "w")


        for self.consulta in enumerate(self.lista):
            self.DADOS_OUTPUT
            arquivo.write("{},{},{},{}\n".format(self.contato["ID"],
                self.contato["nome"], self.contato["email"], self.contato["telefone"]))
        arquivo.close()

    def criar_contato(self):
        while True:
            self.manipular_dados
            print(self.lista)
            self.salvar_contatos()
            option = str(raw_input("Gostaria de aplicar mais um? S ou N"))


            if option == 'N':
                break
                start_agenda()
            else:
                print("OK!")

    def excluir_dados(self):
        print("EXCLUIR TODOS OS DADOS!")
        time.sleep(1)
        self.start_agenda()

    def excluir_dado(self):
        print("EXCLUIR UM DADO!")
        self.start_agenda()

    def metodo_excluir(self):
        print('1 - Excluir um contato')
        print('2 - Excluir todos')
        print('Qualquer numero - Retornar menu')

        option = str(raw_input('Escolha: '))

        if option == '1':
            self.excluir_dado()
        elif option == '2':
            self.excluir_dados()
        else:
            print("Retornando ao menu.")
            self.start_agenda()

    @staticmethod
    def menu():
        print("=" * 30)
        print("=" * 30)
        print("1 - Criar Arquivo")
        print("2 - Criar Contato")
        print("3 - Excluir Contato")
        print("4 - Listar Contatos")
        print("5 - Sair")
        print("=" * 30)

    def start_agenda(self):
        self.menu()
        while True:
            option = int(input("O que você gostaria de fazer? \n"))
            if option == 1:
                self.criar_arquivo()
            elif option == 2:
                self.criar_contato()
            elif option == 3:
                self.metodo_excluir()
            elif option == 4:
                self.ler_arquivo()
                self.listar_contatos()
            elif option == 5:
                break
            elif option == 6:
                self.menu()

            else:
                print("Dado incorreto!")
                print("Digite o 6 para ver o menu novamente.")

    @staticmethod
    def apresentacao():
        print("apresentacao!")
        print("#" * 30)
        print("SEJA BEM VINDO À AGENDA!")
        print("#" * 30)
        time.sleep(1)
        i = 10
        i2 = 2
        while i >= 0:
            print("#" * i2)
            i2 = i2 + 2
            time.sleep(0.1)
            i = i - 1

    @staticmethod
    def creditos():
        print("iniciou!")
        time.sleep(1)
        print("Feito por Nivs.")
        time.sleep(1)
        print("Não passei a semana toda estudando orientação em objetos em Python pra você me plagiar de graça.")
        print("Sai daqui.")

        time.sleep(4)

    def inicio(self):

        self.creditos()
        self.apresentacao()
        self.start_agenda()





agenda = Agenda()


