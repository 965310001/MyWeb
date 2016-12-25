#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('gbk')

import requests
from openpyxl import Workbook
import os

def get_json(url,page,lang_name):
    data={'first':'true','pn':page,'kd':lang_name}
    json = requests.post(url, data).json()
    list_con=json['content']['positionResult']['result']
    list_info=[]
    for list in list_con:
        info=[]
        info.append(list['companyId'])
        info.append(list['positionName'])
        info.append(list['workYear'])
        info.append(list['secondType'])
        info.append(list['education'])
        info.append(list['jobNature'])
        info.append(list['industryField'])
        info.append(list['positionAdvantage'])
        info.append(list['salary'])
        info.append(list['companySize'])
        info.append(list['financeStage'])
        info.append(list['firstType'])
        info.append(list['secondType'])
        info.append(list['companyFullName'])
        info.append(list['city'])
        info.append(list['positionAdvantage'])
        info.append(list['companyShortName'])

        companyLabelList= list['companyLabelList']
        if type(companyLabelList) is []:
            companyLabelListItemInfo=''
            for companyLabelListItem in companyLabelList:
                companyLabelListItemInfo+=companyLabelListItem+','
            info.append(companyLabelListItemInfo)
        list_info.append(info)
        # print list['companyFullName'],list['salary'],list['secondType'],list['firstType']
    return list_info

def main():
    # https: // www.lagou.com / jobs / positionAjax.json?needAddtionalResult = false
    url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    lang_names=['java','PHP','C++','C','Python','Go']
    # lang_names=['html']
    for lang_name in lang_names:
        result_info = []
        page = 1
        while page <= 30:
            info = get_json(url, page, lang_name)
            print(info)
            info.sort()
            result_info += info
            page += 1
        wb = Workbook()
        ws1 = wb.active
        ws1.title = lang_name
        for row in result_info:
            ws1.append(row)

        if os.path.exists(lang_name + '.xlsx'):
            os.remove(lang_name + '.xlsx')
            print ('删除文件成功！',lang_name,'.xlsx')
        wb.save(lang_name + '.xlsx')

    # lang_name='java'
    # page = 1
    # while page <= 30:
    #     info = get_json(url, page, lang_name)
    #     print info
    #     result_info += info
    #     page +=1
    # wb=Workbook()
    # ws1=wb.active
    # ws1.title=lang_name
    # for row in result_info:
    #     ws1.append(row)
    #
    # if os.path.exists(lang_name+'.xlsx') :
    #      os.remove(lang_name + '.xlsx')
    #      print ('删除文件成功！')
    # wb.save(lang_name+'.xlsx')

if __name__=='__main__':
    main()