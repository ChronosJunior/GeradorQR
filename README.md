# Gerador automático de QR Code

## Uso

### Instalação:

primeiro clone o repositório

    git clone https://github.com/ChronosJunior/GeradorQR.git

Com o python já instalado em seu computador, instalaremos os pré requisitos.

_(Opcional)_ Recomendamos a utilização de ambientes virtuais para uma instalação mais limpa:

    cd GeradorQR
    python3 -m venv .venv
    source .venv/bin/activate

Agora instale as bibliotecas necessárias:

    pip install -r requirements.txt

### Uso:

Para utilizar o script, basta executa-lo em um terminal dessa forma:

    main.py <conteudo> <tipo (escolher entre link, texto)>

É possível gerar QR codes utilizando links ou puramente textos. Essa escolha será passada como argumento na hora da execução do script.
