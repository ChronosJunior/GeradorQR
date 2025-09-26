import qrcode
import sys
import requests
import os

def tratar_url(arg):
    if arg.find("https://") == -1 and arg.find("http://") == -1:
        arg = "http://"+arg
    if arg.find(".") == -1:
        arg = arg + ".com"
    return arg

def tratar_texto(arg):
    index_ponto = arg.find(".")
    index_barra = arg.find("/")
    if index_barra != -1:
        arg=arg[0:index_barra]
    if index_ponto != -1:
        arg=arg[0:index_ponto]
    return arg

def testar_url(link):
    print('Função testar_url removida temporariamente para evitar erros em ambientes sem internet.')
    return

    try:
        response = requests.get(link)

        if response.status_code != 200:
            raise Exception("Link inválido...")
    except Exception as e:
        print(e)
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
