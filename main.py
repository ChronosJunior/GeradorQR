import qrcode
import sys


def gerar_qr_code(link):
    img = qrcode.make(link)
    type(img) 
    img.save(link+".png")

def main():
    if len(sys.argv) > 1:
        link = sys.argv[1]
        gerar_qr_code(link)
    else:
        print(f"Uso {sys.argv[0]} <exemplo.com>")

if __name__ == "__main__":
    main()
