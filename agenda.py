import pickle
import os.path

if os.path.isfile("Contatos.arq"):
    fp = open("Contatos.arq", "rb")
    listacon = pickle.load(fp)
    fp.close()
else:
    listacon = [
        [
            'Rena', '(85) 99932-2645', '19/10'
        ],
        [
            'Leonardo', '(85) 99955-7997', '27/10'
        ]
    ]


def menu():
    print('***********************')
    print('* Agenda de telefones *')
    print('***********************')
    print(' ')
    print('1 - BUSCAR contato')
    print('2 - INSERIR contato')
    print('3 - APAGAR contato')
    print('4 - MOSTRAR contatos pelo nome')
    print('5 - MOSTRAR contatos pelo aniversário')
    print(' ')
    print('0 - SAIR do aplicativo')
    print(' ')
    print('Escolha uma opção: ', end=(''))
    return input()


def buscarcontato():
    print('**** Buscar contato ****')
    print ('Nome: ',end='')
    nome = input ()
    resultado = [ x for x in listacon if x[0]==nome]
    if len (resultado):
        contato = resultado [0]
        print("      Telefone: {:16s} Aniversário: {:5s}".format(contato[1], contato[2]))
        print ('\n\n')
    else:
        print ('**** Contato não existe ****')

def inserircontato():
    print ('--- Cria novo contato ---')
    print ('nome: ', end='')
    nomecon = input()
    resultado = [ x for x in listacon if x[0]==nomecon]
    if len (resultado):
        print ('**** Contato existente ****\n')
        return
    print ('Telefone: ', end='')
    telcon = input()
    print ('Aniversário (dd/mm): ', end='')
    nivercon = input()
    print ('Salvar contato? (s/n): ', end='')
    sn = input()
    if sn == 's':
        novocon = [nomecon, telcon, nivercon]
        listacon.append(novocon)
        fp = open('Contatos.arq', 'wb')
        pickle.dump(listacon, fp)
        fp.close()

def apagarcontato():
    print('**** Apagar contato ****')
    print ('Nome: ',end='')
    nome = input ()
    for i in range (len(listacon)):
        if listacon[i][0]==nome:
            print ('Excluir {:1s}? (s/n): '.format(nome), end='')
            sn = input()
            if sn == 's':
                listacon.remove(listacon[i])
                fp = open('Contatos.arq', 'wb')
                pickle.dump(listacon, fp)
                fp.close()
            break
        else:
            print ('**** Contato não existe ****')

def mostrarcontato():
    print ('------------ Lista de contatos ------------')
    print ('NOME---------------- FONE ----------  ANIV')
    for contato in listacon:
         print("{:20s} {:16s} {:5s}".format(contato[0],contato[1], contato[2]))
    print ('\n\n')

def mostrarcontatonome():
    print('MOSTRAR contatos pelo nome \n\n')
    listacon.sort ( key=lambda contato: contato [0] )
    mostrarcontato()

def mostrarcontatoniver():
    print('MOSTRAR contatos pelo aniversário\n\n')
    listacon.sort ( key=lambda contato: contato [2] )
    mostrarcontato()


def principal():
    op = '1'
    while op != 0:
        op = menu()
        if op == '1':
            buscarcontato()
        elif op == '2':
            inserircontato()
        elif op == '3':
            apagarcontato()
        elif op == '4':
            mostrarcontatonome()
        elif op == '5':
            mostrarcontatoniver()
        elif op == '0':
            print('**** APLICATIVO FINALIZADO ****')
            return


principal()
