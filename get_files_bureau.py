import glob
from datetime import datetime
from dateutil.parser import parse as parse_date

for arquivo in glob.glob('/home/thamyres/snap/filezilla/17/*.*'):
    a = open(arquivo, 'r')
    caminho_destino = 'processar.txt'
    with open(caminho_destino, 'a+') as arquivo_destino:
        arquivo_destino.write(f'\n #{arquivo} \n')
    
    lines = a.readlines()
    total_lines = len(lines)
    
    for line_number, lines in enumerate(lines):
        if line_number == 0 or line_number == (total_lines-1):
            continue
        else:
            cpf = lines[1:12]
            contrato = lines[26:50].strip()
            data_solicitacao = lines[56:64]
            data_solicitacao = parse_date(data_solicitacao).strftime('%d/%m/%Y')
            bureau = lines[51:53]
            print(cpf, "|", contrato, '|', data_solicitacao, '|', bureau)

            with open(caminho_destino, 'a+') as arquivo_destino:
                arquivo_destino.write(f'|{cpf}|{contrato}|{data_solicitacao}|{bureau}| \n')
