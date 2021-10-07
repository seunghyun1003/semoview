import requests
import openpyxl

client_id = 'K2vVFQu2QtKpHI9H75Z6' # Your client_id
client_secret = 'SttzUw7IfT' # Your client_secret

start = 1 
num = 0 

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 100
excel_sheet.append(['id', 'stageTitle', 'stageImglink'])

for index in range(10):
    start_num = start + (index * 100)
    naver_open_api = "https://openapi.naver.com/v1/search/shop.json?query=연극&display=100&start=" + str(start_num)
    header_parms = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    res = requests.get(naver_open_api, headers=header_parms)
    res.raise_for_status()
    
    if res.status_code == 200:
        data = res.json()
        for item in data['items']:
            num += 1
            sub = "<b>연극</b>"
            excel_sheet.append((num, item['title'].replace(sub, ' '), item['image']))
    else:
        print("Error : ", res.status_code)

excel_file.save('StageData.xlsx')
excel_file.close()

    
    



