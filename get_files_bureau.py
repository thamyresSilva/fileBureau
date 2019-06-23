import glob
from datetime import datetime
from dateutil.parser import parse


quantos = 0

for arquivo in glob.glob('files/*.*'):
    quantos = quantos + 1
    a = open(arquivo, 'r')
    caminho_destino = 'processar.txt'
    with open(caminho_destino, 'a+') as arquivo_destino:
        arquivo_destino.write(f'#{arquivo}')
    
    lines = a.readlines()

    for line in lines:
        cpf = line[1:12]
        contrato = line[26:50].strip()
        data_solicitacao = line[56:64]
        data_solicitacao = parse(data_solicitacao)
        bureau = line[51:53]
        print(cpf, "|", contrato, '|', data_solicitacao, '|', bureau)
       
        with open(caminho_destino, 'a+') as arquivo_destino:
            arquivo_destino.write(f'|{cpf}|{contrato}|{data_solicitacao}|{bureau}|')

    print('Quantidade de arquivos: ', quantos)