#!/usr/bin/env python3

"""
Hello World Mult Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente

How to use:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Jhonny Rene"
__license__ = "Unlicense"

import os

current_language = "it_IT"
msg = "Hello,World!"

if current_language == "pt_BR":
    msg =  "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"


print(msg)