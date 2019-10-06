import requests
import json
import xmltodict

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSilvTrade'
queryParams = '?' + 'LAWD_CD=' + '41570' \
              + '&DEAL_YMD=' + '201910' \
              + '&ServiceKey=' + 'piLQMdjVMa9MniGNBO8EJ33uVdnBxExDigHFi3LHPYLlhu7JVrb2S7tbcS1cT7sfSR6yjcBo3OqIBplQskTXXg%3D%3D'

result = requests.get(url + queryParams)
file = open('./sise.json', "w+")
file.write(json.dumps(xmltodict.parse(result.content), indent='\t'))
