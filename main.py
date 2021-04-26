import requests

## Já deixei instalado o package do Requests e também importado aqui para você. Está pronto para usar.
## pode apagar esse comentário haha.

## Bom desafio!


print("Bem vindo ao vrificador de Sites")
print('-*'*30)

url = input("Insira as URLs dos sites que deseja verificar o status. (separados por vírgula): \n").strip()

split_url = url.split(",")

print('-*'*30)

url_tratada = []


for url in split_url:
  if "http://"  in url:
    url_formatada = url.strip().lower() 
  else:
    url_formatada = "http://{}".format(url.strip().lower() )
  url_tratada.append(url_formatada)

print("Status:");

for url in url_tratada:
  if ".com"  not in url:
    msg = "URL inválida"
  else:
    status_url = requests.get(url)
    if status_url.status_code != 200:
      msg = "OFFLINE!"
    else:
      msg = "ONLINE!"
  print(f'{url}: {msg}')

