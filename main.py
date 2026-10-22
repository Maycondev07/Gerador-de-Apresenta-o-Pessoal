import time

try:
    txt = open("./apresentação.txt", "a")
    nome = input("Escreva seu nome: ")
    idade = input("Escreva sua idade: ")
    while True:
        assunto = input("Comente brevemente sobre o que gosta: ")
        print (f"Seu texto ficou assim: \n Prazer eu sou {nome.capitalize()}, tenho {idade} anos, e no geral gosto de {assunto.lower()}")
        ask = input("\n Gostaria de salvar? s/n\n").lower()
        if ask == "s".lower():
            txt.write(f"Prazer eu sou {nome.capitalize()}, tenho {idade} anos, e no geral {assunto.lower()}\n")
            print("..")
            time.sleep(0.1)
            print("...")
            time.sleep(0.2)
            print("Texto salvo com sucesso!")
            break
    txt.close()
except:
    txt = open("./apresentação.txt", "w")
    nome = input("Escreva seu nome: ")
    idade = input("Escreva sua idade: ")
    while True:
        assunto = input("Comente brevemente sobre o que gosta: ")
        print (f"Seu texto ficou assim: \n Prazer eu sou {nome.capitalize()}, tenho {idade} anos, e no geral gosto de {assunto.lower()}")
        ask = input("\n Gostaria de salvar? s/n\n")
        if ask == "s".lower():
            txt.write(f"Prazer eu sou {nome.capitalize()}, tenho {idade} anos, e no geral {assunto.lower()}\n")
            print("..")
            time.sleep(0.1)
            print("...")
            time.sleep(0.2)
            print("Texto salvo com sucesso!")
            break
    txt.close()