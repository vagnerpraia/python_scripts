#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 20 de out de 2015

@author: vagnerpraia
'''

import csv
from collections import OrderedDict

def structure_csv(csv_file, path_result):
    secoes = {};
    divisoes = {};
    grupos = {};
    classes = {};
    subclasses = {};
    
    secao_atual = '';
    divisao_atual = '';
    grupo_atual = '';
    classe_atual = '';
    
    
    
    # Leitura do CSV fonte dos dados
    with open(csv_file, 'r', encoding="latin1") as f:
        for row in csv.reader(f):
            
            if (len(row[1]) == 1):
                secoes.update({row[1] : [row[6], []]})
                secao_atual = row[1]
            
            elif (len(row[2]) == 2):
                id_cnae = row[2].replace('.', '').replace('-', '').replace('/', '')
                divisoes.update({id_cnae : [row[6], [secao_atual]]})
                divisao_atual = id_cnae
            
            elif (len(row[3]) == 4):
                id_cnae = row[3].replace('.', '').replace('-', '').replace('/', '')
                grupos.update({id_cnae : [row[6], [secao_atual, divisao_atual]]})
                grupo_atual = id_cnae
            
            elif (len(row[4]) == 7):
                id_cnae = row[4].replace('.', '').replace('-', '').replace('/', '')
                classes.update({id_cnae : [row[6], [secao_atual, divisao_atual, grupo_atual]]})
                classe_atual = id_cnae
            
            elif (len(row[5]) == 9 and '-' in row[5]):
                id_cnae = row[5].replace('.', '').replace('-', '').replace('/', '')
                subclasses.update({id_cnae : [row[6], [secao_atual, divisao_atual, grupo_atual, classe_atual]]})
    
    if (path_result[-1:] not in ['/', '\\']): path_result += '/'
    
    
    
    # Escrita dos arquivos CSV
    with open(path_result + 'secoes_cnae.csv', 'w') as f:
        f.write('id,denominacao\n')
        for k, v in OrderedDict(sorted(secoes.items())).items():
            f.write('"' + k + '","' + v[0] + '"\n')
    
    with open(path_result + 'divisoes_cnae.csv', 'w') as f:
        f.write('id,denominacao,secao\n')
        for k, v in OrderedDict(sorted(divisoes.items())).items():
            f.write('"' + k + '","' + v[0] + '","' + v[1][0] + '\n')    
    
    with open(path_result + 'grupos_cnae.csv', 'w') as f:
        f.write('id,denominacao,secao,divisao\n')
        for k, v in OrderedDict(sorted(grupos.items())).items():
            f.write('"' + k + '","' + v[0] + '","' + v[1][0] + '","' + v[1][1] + '"\n')    
    
    with open(path_result + 'classes_cnae.csv', 'w') as f:
        f.write('id,denominacao,secao,divisao,grupo\n')
        for k, v in OrderedDict(sorted(classes.items())).items():
            f.write('"' + k + '","' + v[0] + '","' + v[1][0] + '","' + v[1][1] + '","' + v[1][2] + '"\n')    
    
    with open(path_result + 'subclasses_cnae.csv', 'w') as f:
        f.write('id,denominacao,secao,divisao,grupo,classe\n')
        for k, v in OrderedDict(sorted(subclasses.items())).items():
            f.write('"' + k + '","' + v[0] + '","' + v[1][0] + '","' + v[1][1] + '","' + v[1][2] + '","' + v[1][3] + '"\n')
    
    
    
    #Escrita dos arquivos SQL
    with open(path_result + 'classes_cnae.sql', 'w') as f:
        for k, v in OrderedDict(sorted(classes.items())).items():
            f.write('INSERT INTO syst.dc_classe_atividade_economica (cd_classe_atividade_economica, tx_classe_atividade_economica) VALUES (\'' + k + '\', \'' + v[0] + '\');\n')    
    
    with open(path_result + 'subclasses_cnae.sql', 'w') as f:
        for k, v in OrderedDict(sorted(subclasses.items())).items():
            f.write('INSERT INTO syst.dc_subclasse_atividade_economica (cd_subclasse_atividade_economica, cd_classe_atividade_economica, tx_subclasse_atividade_economica) VALUES (\'' + k + '\', \'' + v[1][3] + '\', \'' + v[0] + '\');\n')
    
    print('Mission accomplished')
    
structure_csv('D:/Users/vagnerpraia/Documents/Ipea/Plataformas da cidadania/Base de Dados/CNAE/Subclasses CNAE 2.2 - Estrutura.csv', 'D:/Users/vagnerpraia/Documents/Ipea/Plataformas da cidadania/Base de Dados/CNAE')