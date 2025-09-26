import qrcode
import sys
import requests
import os

def tratar_url(arg):
    if arg.find("https://") == -1 or arg.find("http://") == -1:
        arg = "https://"+arg
    if arg.find(".") == -1:
        arg = arg + ".com"
    return arg

def tratar_texto(arg):
    print(arg)
    index_ponto = arg.find(".")
    index_barra = arg.find("/")
    if index_barra != -1:
        arg=arg[0:index_barra]
    if index_ponto != -1:
        arg=arg[0:index_ponto]
    print(arg)
    return arg

def testar_url(link):
    try:
        response = requests.get(link)
    except:
        print("Link inválido...")
        exit()

def gerar_qr_code(*conteudo):
    if len(conteudo) == 2:
        img = qrcode.make(conteudo[1])
    else:
        img = qrcode.make(conteudo[0])
    type(img) 
    nome_arquivo_gerado=conteudo[0]+".png"
    img.save(nome_arquivo_gerado)
    print(f"QRCode gerado e salvo em: {os.getcwd()}/{nome_arquivo_gerado}")

def main():
    if len(sys.argv) > 2:
        conteudo = sys.argv[1]
        if sys.argv[2] == "link":
            url = tratar_url(conteudo)
            testar_url(url)
        conteudo=tratar_texto(conteudo)
        gerar_qr_code(conteudo, url)
    else:
        print(f"Uso {sys.argv[0]} <conteudo> <tipo (escolher entre link, texto)>")

if __name__ == "__main__":
    main()
