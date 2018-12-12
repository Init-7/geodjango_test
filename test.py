CONNETCTUS_URL ='https://api.connectus.cl/api_v1/send_sms'
CONNECTUS_ACCOUNT_SID = '9e01f41122384f5ea9192ade9d1c1c0c'
CONNECTUS_AUTH_TOKEN = '4ba4d39de3c14a8099c4b5cf0a1cab19'

params = dict()
params['dst_number']=5685567407
params['sms_content']='Hola Mundo!'

response = requests.post(CONNETCTUS_URL, params = params, auth=(CONNECTUS_ACCOUNT_SID,CONNECTUS_ACCOUNT_SID))

print response
