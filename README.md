# Keylogger Simulado em Python

Este repositório reúne os testes práticos que desenvolvi durante os meus estudos de cibersegurança para entender, na prática, como funciona um keylogger simples em Python e, principalmente, como podemos identificar e nos proteger desse tipo de ameaça.

> **Importante:** Todo o código aqui tem finalidade **100% educacional**. Os testes foram feitos apenas na minha própria máquina, em ambiente controlado e com dados fictícios.

## Sobre o experimento

Durante as aulas, o objetivo era compreender como um script consegue capturar eventos do teclado e automatizar o envio dessas informações. Dividi meus testes em etapas para acompanhar o funcionamento passo a passo:

* **Captura básica (`keylogger.py`):** primeiro testei o registro simples de teclas para entender como a biblioteca `pynput` escuta o que é digitado e trata teclas especiais, como espaço, enter e backspace.
* **Envio automatizado por e-mail (`keylogger_email.py`):** depois, implementei uma rotina que guarda o texto capturado temporariamente na memória e envia os dados por e-mail de tempos em tempos usando `smtplib` e `Timer`.
* **Evidências (`images/`):** separei o print comprovando o recebimento do e-mail de teste durante a execução controlada.

## O que aprendi na prática

* **Como o código funciona:** o `keyboard.Listener` fica observando cada tecla pressionada e vai montando o texto em uma variável (`log`). A cada intervalo definido pelo `Timer`, o script verifica se existe conteúdo novo, conecta ao servidor SMTP com criptografia TLS, envia o e-mail e limpa a variável para o próximo ciclo.
* **Cuidado com credenciais:** durante os testes locais utilizei uma senha de aplicativo do Gmail para validar o envio, mas antes de subir o projeto para o GitHub removi a credencial real e deixei apenas um espaço de exemplo (`SUA_SENHA_DE_APP_AQUI`). Em qualquer projeto de segurança, proteger senhas e chaves é essencial.

## Como se proteger contra keyloggers

Entender como a ameaça é construída ajuda muito a pensar na defesa. Algumas medidas essenciais no dia a dia e em ambientes corporativos são:

* **Antivírus e EDR atualizados:** ferramentas modernas conseguem detectar comportamentos suspeitos, como programas tentando monitorar o teclado globalmente.
* **Firewall e monitoramento de rede:** ajudam a bloquear ou alertar quando um programa desconhecido tenta abrir conexões de saída (como envios SMTP inesperados).
* **Ambiente isolado (Sandboxing / Máquinas Virtuais):** sempre rodar testes ou arquivos suspeitos em ambientes isolados, nunca direto na máquina principal sem controle.
* **Boas práticas e conscientização:** desconfiar de anexos e links desconhecidos, ativar a autenticação em duas etapas (MFA) e evitar instalar programas de fontes não confiáveis.