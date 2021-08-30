# -*- coding: utf-8 -*-

#NOME: Nivan José dos Santos Junior
#RA:
#CURSO: Engenharia de Software
#SEMESTRE: 2°

import time
import re




class Agenda(object):


    #__INIT__ É CONSIDERADO A "PORTA DE ENTRADA" DE UMA CLASSE. ONDE SÃO INSERIDOS AS VARIAVEIS QUE TERÃO ESCOPO GERAL.
    def __init__(self):

        self.lista = []

        self.ID = 0

        self.contato = {}

        self.inicio()


    #ESTRUTURA DO PEDIDO DE OUTPUT
    @property
    def DADOS_INPUT(self):

        print("*" * 30)

        self.nome = str(raw_input("Digite o nome: ")).lower()

        if len(self.lista) > 0:
            for self.contato in self.lista:
                while True:
                    if self.contato["nome"] == self.nome:
                        print("Esse nome já existe!")
                        self.nome = str(raw_input("Digite o nome: ")).lower()
                    else:
                        break
        else:
            pass
        self.contato = {
            "ID": self.ID + 1,
            "nome": self.nome,
            "email": str(raw_input("Digite o email:")).lower(),
            "telefone": str(raw_input("Digite o telefone: ")).lower(),
            "instagram": str(raw_input("Digite o instagram: ")).lower(),
            "facebook": str(raw_input("Digite o Facebook: ")).lower()
            }

        return self



    def MODIFICA_INPUT(self, nome):
        for self.contato in self.lista:
            print("=" * 30)
            print("-" * 30)
            while True:
                if nome == self.contato["nome"]:

                    self.contato["nome"] = str(raw_input("Digite o novo nome: ")).lower()
                    self.contato["email"] = str(raw_input("Digite o novo email:")).lower()
                    self.contato["telefone"] = str(raw_input("Digite o novo telefone: ")).lower()
                    self.contato["instagram"] = str(raw_input("Digite o novo instagram: ")).lower()
                    self.contato["facebook"] = str(raw_input("Digite o novo Facebook: ")).lower()
                    self.ESTRUTURA_OUTPUT()
                    print("Modificado!")
                    break
                else:
                    print("Não existe esse contato.")
                    break



    #ESTRUTURA DO QUE SERÁ VISTO.
    def ESTRUTURA_OUTPUT(self):
        print("=" * 30)
        print("ID: {}".format(self.contato["ID"]))
        print("-" * 30)
        print("\tNome: {}".format(self.contato["nome"]))
        print("\tEmail: {}".format(self.contato["email"]))
        print("\tTelefone: {}".format(self.contato["telefone"]))
        print("\tInstagram: {}".format(self.contato["instagram"]))
        print("\tFacebook: {}".format(self.contato["facebook"]))
        print("=" * 30)


    #VERIFICAÇÃO SE JÁ EXISTE CERTOS DADOS.
    #EM CONSTRUÇÃO
    def verifica_dado(self, dado):
        if len(self.lista) > 0:
            for self.contato in self.lista:
                if self.contato[dado] == self.nome:
                    return False
        return True



    #AQUI INTEGRA OS DICIONÁRIOS À LISTA
    @property
    def manipular_dados(self):
       return self.lista.append(self.contato)



    #ALGORITMO PARA GERAR O NOME DO ARQUIVO
    @property
    def gerar_nome_arquivo(self):
        arquivo = raw_input("Digite o nome do seu arquivo.")
        formato = raw_input("Digite o formato. .txt ou .csv?")
        out = re.sub(r'[^\w\s+$]', '', arquivo)
        out2 = re.sub(r'[^\w\s+$]', '', formato)
        self.nome_arquivo = str("{}.{}".format(out, out2))
        return self

    #CASO NÃO HAJA UM ARQUIVO, AQUI É POSSIVEL CRIAR, INCLUINDO A DECLARAÇÃO DO NOME DO ARQUIVO
    def criar_arquivo(self):

        self.gerar_nome_arquivo
        print("COMO FICOU O NOME DO ARQUIVO:")
        print(self.nome_arquivo)
        time.sleep(2)
        open(str(self.nome_arquivo), "a")
        print("ARQUIVO CRIADO!")
        self.start_agenda()

    #AQUI LE O ARQUIVO EXTERNO
    def ler_arquivo(self):
        arquivo = open("agenda.txt", 'r')
        try:
            for self.lista in arquivo.readlines():
                coluna = self.lista.strip().split(",")

                self.contato = {
                    "ID": coluna[0],
                    "nome": coluna[1],
                    "email": coluna[2],
                    "telefone": coluna[3]
                }

            arquivo.close()

        except:
            pass
            print(self.lista)

    #FAZ O LAYOUT DA LISTA QUE SERÁ MOSTRADA AQUI.
    #PARA NÃO MOSTRAR APENAS SIMPLES LISTAS E DICTS.
    def mostrar_lista(self):
        if len(self.lista) > 0:
            for index, self.contato in enumerate(self.lista):
                print("\n")
                print("=" * 30)
                self.ESTRUTURA_OUTPUT()
                print("")
                time.sleep(0.2)
            print("Quantidade de contatos: {}\n".format(len(self.lista)))

        else:
                print("Não existe nenhum contato cadastrado para listar.\n")

    #SALVA OS CONTATOS NUM ARQUIVO EXTERNO
    def salvar_contatos(self):
        arquivo = open("agenda.txt", "w")
        for self.contato in self.lista:

            arquivo.write("{},{},{},{}\t".format(
                self.contato["ID"],
                self.contato["nome"],
                self.contato["email"],
                self.contato["telefone"]))



    #BUSCA POR MEIO DO NOME ALGUM INDICE DA LISTA, QUE RETORNA UM DICIONÁRIO
    def buscar_contato(self):

                if len(self.lista) > 0:
                    print("-_" * 10 + " Buscar ou Excluir Contato " + "-_" * 10)


                    nome = str(raw_input("Digite o nome do contato a ser encontrado: \n")).lower()


                    for self.contato in self.lista:
                        if self.contato["nome"] == nome:
                            self.ESTRUTURA_OUTPUT()

                            option = str(raw_input("Você deseja modificar? S ou N")).upper()
                            if option == "S":
                                self.MODIFICA_INPUT(nome)
                            else:
                                pass
                        else:
                            pass
                            #print("Não existe esse contato.")
                else:
                    print("Não há registros. Ainda.")
                    time.sleep(1)
                    self.start_agenda()
                return self

    #UM DOS CAMINHOS DO METODO_EXCLUIR
    def excluir_dados(self):
        option = str(raw_input("Você tem certeza? S ou N")).upper()
        if option == "S":
            if len(self.lista) > 0:

                print("EXCLUIR TODOS OS DADOS!")
                del self.lista
                self.lista = []
                self.contato = {}
                time.sleep(1)
                self.start_agenda()
            else:
                print("Não tem nada para excluir.")
                print("Adicione algo.")
                option2 = str(raw_input("Deseja criar os primeiros contatos da sua agenda? S ou N")).upper()
                if option2 == "S":
                    print("=" * 60)
                    self.criar_contato()

        elif option == "N":
            print("Ufa. Achei que tu tava ficando doido.")
            self.start_agenda()
        else:
            print("COLOQUE DIREITO OS DADOS!")

    #UM DOS CAMINHOS DO METODO_EXCLUIR
    def excluir_dado(self):
        print("EXCLUIR UM DADO!")
        print("DISPONIVEIS PARA EXCLUSÃO: {} CONTATOS.".format(self.ID))
        while True:
            if self.ID > 0:
                print("*" * 30 + " Excluir um Contato " + "*" * 30)


                while True:
                    for self.contato in self.lista:
                        nome = str(raw_input("Digite o nome do contato a ser encontrado: ")).lower()
                        if self.contato["nome"] == nome:
                            i = self.contato["ID"] - 1
                            print(self.ID)
                            self.ESTRUTURA_OUTPUT()

                            option = str(raw_input("Você tem certeza que deseja excluir?")).upper()
                            if option == "S":
                                while True:
                                    try:
                                        lista = len(self.lista) - 1
                                        del self.lista[i]
                                        if len(self.lista) <= 1:
                                            print("Um foi excluido. {} contato disponivel.".format(lista))
                                            break
                                        else:
                                            print("Um foi excluido. {} contatos disponiveis.".format(lista))
                                            break
                                    except IndexError:
                                        print("Não existe mais contatos.")
                                        break
                                        self.start_agenda()

                            else:
                                break
                        else:
                            print("Esse nome não existe na Agenda.")
                            option2 = str(raw_input("Deseja tentar de novo? S ou N")).upper()
                            if option2 == 'N':
                                break
                                self.start_agenda()
                            else:
                                break


            else:
                print("Não há registros. Ainda.")
                time.sleep(1)
                break
                self.start_agenda()

        self.start_agenda()

    #METODO EXCLUIR ONDE RETORNA 2 CAMINHOS: EXCLUIR UM OU EXCLUIR TODOS.
    def metodo_excluir(self):
        print("*" * 30 + " Excluir " + "*" * 30)
        print("#" * 60)
        print("DISPONIVEIS PARA EXCLUSÃO: {} CONTATOS.".format(self.ID))
        print('1 - Excluir um contato')
        print('2 - Excluir todos')
        print('Qualquer numero - Retornar menu')

        option = int(raw_input('Escolha: '))

        if option == 1:
            self.excluir_dado()
        elif option == 2:
            self.excluir_dados()
        else:
            print("Retornando ao menu.")
            self.start_agenda()


    #ISTANCIA DE CRIAÇÃO DE CONTATO.
    #ESTRUTURA QUE SE CONECTA COM DIVERSOS METODOS E RETORNOS DE DADOS
    def criar_contato(self):

        print("-_" * 10 + " Criar Contato " + "-_" * 10)

        while True:


            while True:
                try:
                    option2 = int(raw_input("Gostaria de adicionar quantos?"))
                    break
                except ValueError:
                    print("Válido somente numeros!")

            while option2 >= 1:
                self.DADOS_INPUT
                option2 = option2 - 1
                self.ID = self.ID + 1
                self.manipular_dados
                self.salvar_contatos()




            self.mostrar_lista()

            option = str(raw_input("Gostaria de adicionar mais? S ou N"))


            if option == 'N':
                break
                print("Para ver menu novamente, APERTE 6!")
                self.start_agenda()
            else:
                print("OK!")

    #MENU ESTÁTICO
    @staticmethod
    def menu():
        print("=" * 30)
        print("=" * 30)
        print('''   
        
        1 - Criar Contato
        2 - Excluir Contato
        3 - Listar Contatos
        4 - Buscar Contato e/ou modifica-lo
        5 - Sair
        6 - [BÔNUS] Criar Arquivo 
                    
                ''')


        print("=" * 30)

    #A FUNÇÃO DE DIRECIONAMENTO DO USUÁRIO. UMA DOS PRINCIPAIS MÉTODOS DA CLASSE.
    #ONDE HÁ A INTEGRAÇÃO PRINCIPAL DAS INSTÂNCIAS.
    def start_agenda(self):
        print("*" * 30 + " COMEÇO DA AGENDA. SEJA BEM VINDO! " + "*" * 30)
        print("*" * 95)

        while True:
            self.menu()
            while True:
                try:
                    option = int(input("O que você gostaria de fazer? \n"))
                    break
                except NameError:
                    print("\nAceito apenas números!\n")

            if option == 1:
                self.criar_contato()
            elif option == 2:
                self.metodo_excluir()
            elif option == 3:
                self.mostrar_lista()
                time.sleep(3)
            elif option == 4:
                self.buscar_contato()
            elif option == 5:
                self.fim()
                break
            elif option == 6:
                self.criar_arquivo()
            else:
                print("Dado incorreto!")
                print("Digite o 6 para ver o menu novamente.")

    #APRESENTAÇÃO INICIAL DA AGENDA.
    @staticmethod
    def apresentacao():
        print("apresentacao!")
        print("#" * 30)
        print("SEJA BEM VINDO À AGENDA!")
        print("#" * 30)
        time.sleep(1)
        i = 14
        i2 = 30
        while i >= 0:
            print("#" * i2)
            i2 = i2 - 2
            time.sleep(0.1)
            i = i - 1

    #DESPEDIDA/EXIT
    @staticmethod
    def fim():
        print("Espero que a agenda tenha sido útil.")
        print("Até a próxima.")
    #CREDITOS DO NIVS
    @staticmethod
    def creditos():
        print("iniciou!")
        time.sleep(1)
        print("Feito por Nivs.")
        time.sleep(1)
        print("Não passei a semana toda estudando orientação em objetos em Python pra você me plagiar de graça.")
        time.sleep(1)
        print("Sai daqui.")
        time.sleep(4)

    #PRIMEIRA CAMADA INICIAL
    #ORGANIZAÇÃO DE CRÉDITOS, APRESENTAÇÃO INICIAL, E INICIO DO ALGORITMO
    def inicio(self):

        #self.creditos()
        #self.apresentacao()

        self.start_agenda()


agenda = Agenda()
