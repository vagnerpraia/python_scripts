#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 20 de out de 2015

@author: vagnerpraia
'''

import csv

def read_csv(path_csv, path_sql = '', header = True, columns = {}):
    
    with open(path_csv, 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        
        flag_head = header
        position_column = {}
        line_count = 0;
        values = {}
        
        for row in reader:
            if flag_head:
                if len(columns) == 0:
                    for r in row:
                        position_column.update({row.index(r) : [r, 'string']})
                else:
                    for r in [x.strip() for x in row]:
                        if r in columns.keys():
                            position_column.update({row.index(r) : [r, columns.get(r)]})
                flag_head = False
                line_count += 1
                
            else:
                v = ''
                for r in [x for x in row if row.index(x) in position_column]:
                    if position_column.get(row.index(r))[1] == 'numeric' :
                        v += r.strip() + ', '
                    else:
                        v += '\'' + r.strip() + '\', '
                values.update({line_count : v[:-2]})    
                line_count += 1
    
    with open(path_sql, 'w') as f:
        for v in values.values():
            f.write('INSERT INTO test (' + str(columns.keys())[11:-2] + ') VALUES (' + str(v) + ');\n')
    
read_csv('D:/Users/vagnerpraia/Workspace/Eclipse/python_apps/test/test2.csv', 'D:/Users/vagnerpraia/Workspace/Eclipse/python_apps/test/test2.sql', True, {'bosc_sq_osc' : 'numeric', 'mdfd_cd_fonte_dados' : 'numeric', 'loca_ds_endereco' : 'string', 'loca_ds_endereco_complemento' : 'string', 'loca_nm_bairro' : 'string', 'edmu_cd_municipio' : 'numeric', 'loca_geometry' : 'numeric', 'loca_nm_cep' : 'numeric', 'loca_ds_endereco_corrigido' : 'string', 'loca_nm_bairro_encontrado' : 'string', 'gcod_cd_fonte_geocodificacao' : 'string', 'loca_dt_geocodificacao' : 'string'})