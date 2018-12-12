import requests
url = 'https://api.connectus.cl/api_v1/send_sms'
params = dict()
params['dst_number'] = 5685567407
params['sms_content'] = 'Con Connectus es muy facil integrar aplicaciones.'
response = requests.post(url, params=params, auth=('9e01f41122384f5ea9192ade9d1c1c0c', '4ba4d39de3c14a8099c4b5cf0a1cab19'))
