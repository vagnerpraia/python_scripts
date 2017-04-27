# -*- coding: iso-8859-1 -*-

'''
Created on 2 de out de 2016

@author: vagnerpraia
'''

import os
import sys
from csv import reader
from util import find_between

def adjust_string(string):
    string = string.replace('"', '')
    string = string.replace('\'', '')
    string = string.replace('-', '_')
    string = string.replace('$', '(CIFRÃƒO)')
    string = string.replace('%', '(PORCENTO)')
    string = string.replace('...', '.')
    string = string.replace('*', '')
    if string == '': string = ' '
    return string

def convert_file(path_interview_file, path_csv_file, path_result_file = None):
    interview_dict = {}
    csv_header_list = []
    csv_values_dict = {}
    
    if path_result_file is None:
        path_result_file = os.path.dirname(path_interview_file) + '/result.txt'
    
    # Leitura do arquivo de entrevista do Atlas
    flag = True
    list_rows = [x.replace('\n','') for x in open(path_interview_file).readlines()[15:] if x.split() != '\n']
    for row in list_rows:
        if '   (Super)' in row and flag:
            key_interview = find_between(row, ':', ' - ').strip()
            
        else:
            if row[0:6] != 'Codes:' and row[0:8] != 'No memos' and row != '':
                if interview_dict.has_key(key_interview):
                    row_list = interview_dict.get(key_interview)
                    row_list.append(row)
                    interview_dict.update({key_interview : row_list})
                else:
                    interview_dict.update({key_interview : [row]})
                flag = True
    
    # Leitura do arquivo CSV
    flag_header = True
    with open(path_csv_file, 'r') as f:
        for row in reader(f, delimiter = ';'):
            if flag_header:
                csv_header_list.extend(row)
            else:
                count_columns = 0
                csv_values_list = []
                for column in row:
                    value_output = [count_columns, column]
                    csv_values_list.append(value_output)
                    count_columns += 1
                
                csv_values_dict.update({row[0] : csv_values_list})
            
            flag_header = False
    
    # Prepara os cabeçalhos
    header = {}
    flag_header_vazio = True
    for key_interview in interview_dict.keys():
        value_write = ''
        value_write_vazio = ''
        key_interview = find_between(key_interview, '', '.').strip()
        if csv_values_dict.has_key(key_interview):
            for csv_list in csv_values_dict.get(key_interview):
                if flag_header_vazio:
                    value_write_vazio += ' *' + csv_header_list[csv_list[0]] + '_'
                
                value_write += ' *' + csv_header_list[csv_list[0]] + '_' + csv_list[1]
                if (csv_list[0] + 1) == len(csv_header_list):
                    if flag_header_vazio:
                        header.update({'vazio' : '****' + value_write_vazio.decode("latin1").encode("utf8") + '\n'})
                    
                    header.update({key_interview : '****' + value_write.decode("latin1").encode("utf8") + '\n'})
        flag_header_vazio = False
    
    # Escrita do arquivo resultado
    with open(path_result_file, 'w') as f:
        f.write('\n')
        for key_interview, value_interview in interview_dict.items():
            for value in value_interview:
                if header.has_key(key_interview):
                    f.write(header.get(key_interview))
                else:
                    f.write(header.get('vazio'))
                f.write(str(value) + '\n')



if len(sys.argv) == 2 and sys.argv[1] == 'help':
    print 'Para utilizar o programa é necessário a passagem dos seguintes parâmetros:'
    print '\n    Parâmetro 1 = Endereço do arquivo output do software Atlas.ti'
    print '    Parâmetro 2 = Endereço do arquivo CSV com as escalas sociais'
    print '    Parâmetro 3 (Opcional) = Diretório para onde o arquivo com o resultado do processamento será gravado'
    print '\nObs.: Caso o parâmetro 3 não seja passado, o arquivo com o resultado do processamento será gravado no diretório do arquivo do parâmetro 1.'
    print '\n\nExemplo:'
    print '\n    ' + sys.argv[0] + ' C:/PBF_quotes.txt C:/escala social csv.csv C:/IRaMuTeq'
    
elif len(sys.argv) == 3:
    convert_file(sys.argv[1], sys.argv[2])
    
elif len(sys.argv) == 4:
    convert_file(sys.argv[1], sys.argv[2], sys.argv[3])
    
else:
    print 'Comando inválido. Utilize o comando \'' + sys.argv[0] + ' help\' para ter mais informações.'
