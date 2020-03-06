import re
import requests

#coletando sites que deseja analisar
print("Entre com a url completa do site que deseja checar subdomínios: ")
leiaStr = input()



url = requests.get(leiaStr)
result = url.text
###this is return all html text



#dir (requests)
text_regex = result

m = re.findall(r'https://(.*?)/', text_regex)
#m = re.findall(r"https://.*.+\/", text_regex).
#oi = m.search("https://.*?",m)

unique_elements_list=list(set(m))
print(unique_elements_list)