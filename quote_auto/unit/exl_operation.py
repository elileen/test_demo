# -*- coding: utf-8 -*-
# Datetime： 2021-04-13 16:33 
# Author： elileen
# QQ：2049146393
import xlrd


class ExlOperation:

    def __init__(self,path=None,sheet_name=None):
        if path==None:
            path='../../config/logincase.xlsx'
        else:
            path=path
        if sheet_name==None:
            sheet_name = '用例参数'
        else:
            sheet_name=sheet_name
        # 打开表格
        self.workbook=xlrd.open_workbook(path)
        self.sheet=self.workbook.sheet_by_name(sheet_name)

    # 获取行
    def get_rows(self):
        return self.sheet.nrows

    # 获取列
    def get_cols(self):
        return self.sheet.ncols


    ''' 单元格格式判断 '''
    # ctype: 0
    # empty, 1
    # string, 2
    # number, 3
    # date, 4
    # boolean, 5
    # error
    # sheet.cell(row, col).ctype

    '''获取单元格内容'''
    def get_cell_value(self,row,col):
        text=self.sheet.cell_value(row,col)
        if text=='None':
            return ''
        else:
            return self.sheet.cell_value(row,col)

# ex_op=ExlOperation()
# print(ex_op.get_cell_value(1,2))