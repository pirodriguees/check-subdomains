import re
import requests

#input of website for colet subdomains
print("Entre com a url completa do site que deseja checar subdomínios: ")
leiaStr = input()



url = requests.get(leiaStr)
result_html = url.text
###this is return all html text


regex_sites = re.findall(r'https://(.*?)/', result_html)
#regex in all that is inside "https and /"


unique_elements_list=list(set(regex_sites))
print(unique_elements_list)