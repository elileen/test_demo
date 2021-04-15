# -*- coding: utf-8 -*-
# Datetime： 2021-04-14 11:26 
# Author： elileen
# QQ：2049146393
import yaml


class YamlOperation:
    def __init__(self,path='../config/AutoCase.yml'):
        with open(path,'r+',encoding='utf8') as file:
            self.data=yaml.load(file,Loader=yaml.FullLoader)

    # 想要获取的元素
    def get_locator(self,page,locator_name):
        return self.data[page][locator_name]

# yamlOP=YamlOperation('../../quote_auto/config/AutoCase.yml')
# yamlOP=YamlOperation('../config/AutoCase.yml')
# print(yamlOP.get_locator('CustomerPage','addcuswindow'))