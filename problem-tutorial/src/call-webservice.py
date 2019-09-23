from suds.client import Client
from suds.wsse import *

url = "https://xxxx?wsdl"
client = Client(url)
print(client)
security = Security()
token = UsernameToken('user_name', 'password')
security.tokens.append(token)
client.set_options(wsse=security)
# param1 = client.factory.create('ns0:EventObjectType')
# print param1
# param2 = client.factory.create('ns0:Business_Process_DataType')
# print param2
# id_type = client.factory.create('ns0:EventObjectIDType')
# id_type = {'value': '', 'type': 'WID'}
id_type = {'value': ''}
id = [id_type]
event_obj = {'ID': id}
business_process = {'comment': ''}
content = client.service.Approve_Business_Process(event_obj, business_process)
print(content)
# param2 = 'test'
# param1_content = client.factory.create('ns0:EventObjectIDType')
# print param1_content
# param1_content.value = 'ea2a2d7b6e1c0180715d3a9db5567209'
# param1_content._type = 'WID'
# param1.ID.append(param1_content)
# result = client.service.Approve_Business_Process(param1, param2)
