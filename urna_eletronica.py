# CRIAÇÃO DE UMA URNA ELETRÔNICA UTILIZANDO PYTHON

import os

estado = "menu"

def nomeloja():
    print("""
♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡

             V O T E
             A Q U I

♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡
""")

# Quantidade de votos na categoria MENINAS MALVADAS
quant_votos_regina = 0
quant_votos_cady = 0
quant_votos_gretchen = 0
quant_votos_brancos_meninas_malvadas = 0
quant_votos_nulos_meninas_malvadas = 0

def votacao_meninas_malvadas():
    global quant_votos_regina, quant_votos_cady, quant_votos_gretchen, quant_votos_brancos_meninas_malvadas, quant_votos_nulos_meninas_malvadas
    print("💗 Meninas Malvadas")
    print("Quem você escolheria? 💅")
    print("11111 - Regina George 👑")
    print("22222 - Cady Heron 💕")
    print("33333 - Gretchen Wieners 💄")
    print("0 - Voto em Branco ⚪")
    print("Qualquer outro Número - Voto Nulo")
    print("")
    
    while True:
        escolha_meninas_malvadas = int(input("Insira o número do candidato que você escolheu: "))
        if escolha_meninas_malvadas == 11111:
            print("Você apertou para votar em 11111 - Regina George 👑")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 11111 - Regina George 👑")
                quant_votos_regina = quant_votos_regina + 1
                break
        elif escolha_meninas_malvadas == 22222:
            print("Você apertou para votar em 22222 - Cady Heron 💕")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 22222 - Cady Heron 💕")
                quant_votos_cady = quant_votos_cady + 1
                break
        elif escolha_meninas_malvadas == 33333:
            print("Você apertou para votar em 33333 - Gretchen Wieners 💄")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 33333 - Gretchen Wieners 💄")
                quant_votos_gretchen = quant_votos_gretchen + 1 
                break
        elif escolha_meninas_malvadas == 0:
            print("Você apertou para votar em Branco ⚪")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em Branco")
                quant_votos_brancos_meninas_malvadas = quant_votos_brancos_meninas_malvadas + 1
                break
        else:
            print("Você apertou para votar NULO")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's':
                print("Você votou Nulo")
                quant_votos_nulos_meninas_malvadas = quant_votos_nulos_meninas_malvadas + 1  
                break

# Quantidade de votos na categoria MENTALISTA
quant_votos_patrick = 0
quant_votos_teresa = 0
quant_votos_cho = 0
quant_votos_brancos_mentalista = 0
quant_votos_nulos_mentalista = 0

def votacao_mentalista():
    global quant_votos_patrick, quant_votos_teresa, quant_votos_cho, quant_votos_brancos_mentalista, quant_votos_nulos_mentalista
    print("🧠 O MENTALISTA")
    print("Qual personagem você prefere? 🔎")
    print("1111 - Patrick Jane 🖤")
    print("2222 - Teresa Lisbon 👮‍♀️")
    print("3333 - Kimball Cho 💼")
    print("0 - Voto em Branco ⚪")
    print("Qualquer outro Número - Voto Nulo")
    print("")
    
    while True:
        escolha = int(input("Insira o número do candidato que você escolheu: "))
        if escolha == 1111:
            print("Você apertou para votar em 1111 - Patrick Jane 🖤")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 1111 - Patrick Jane 🖤")
                quant_votos_patrick = quant_votos_patrick + 1
                break
        elif escolha == 2222:
            print("Você apertou para votar em 2222 - Teresa Lisbon 👮‍♀️")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 2222 - Teresa Lisbon 👮‍♀️")
                quant_votos_teresa = quant_votos_teresa + 1
                break
        elif escolha == 3333:
            print("Você apertou para votar em 3333 - Kimball Cho 💼")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 3333 - Kimball Cho 💼")
                quant_votos_cho = quant_votos_cho + 1 
                break
        elif escolha == 0:
            print("Você apertou para votar em Branco ⚪")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em Branco")
                quant_votos_brancos_mentalista = quant_votos_brancos_mentalista + 1
                break
        else:
            print("Você apertou para votar NULO")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's':
                print("Você votou Nulo")
                quant_votos_nulos_mentalista = quant_votos_nulos_mentalista + 1  
                break

# Quantidade de votos nas categoria de stranger things 
quant_votos_eleven = 0
quant_votos_eddie = 0
quant_votos_steve = 0
quant_votos_brancos_stranger_things = 0
quant_votos_nulos_stranger_things = 0

def votacao_stranger_things():
    global quant_votos_eleven, quant_votos_eddie, quant_votos_steve, quant_votos_brancos_stranger_things, quant_votos_nulos_stranger_things
    print("👾 STRANGER THINGS")
    print("Quem é o seu favorito? 👀")
    print("11 - Eleven 🧇")
    print("22 - Eddie Munson 🎸")
    print("33 - Steve Harrington 🧢 ")
    print("0 - Voto em Branco ⚪")
    print("Qualquer outro Número - Voto Nulo")
    print("")

    while True:
        escolha = int(input("Insira o número do candidato que você escolheu: "))
        if escolha == 11:
            print("Você apertou para votar em 11 - Eleven 🧇")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 11 - Eleven 🧇")
                quant_votos_eleven = quant_votos_eleven + 1
                break
        elif escolha == 22:
            print("Você apertou para votar em 22 - Eddie Munson 🎸")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 22 - Eddie Munson 🎸")
                quant_votos_eddie = quant_votos_eddie + 1
                break
        elif escolha == 33:
            print("Você apertou para votar em 33 - Steve Harrington 🧢 ")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 33 - Steve Harrington 🧢 ")
                quant_votos_steve = quant_votos_steve + 1 
                break
        elif escolha == 0:
            print("Você apertou para votar em Branco ⚪")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em Branco")
                quant_votos_brancos_stranger_things = quant_votos_brancos_stranger_things + 1
                break
        else:
            print("Você apertou para votar NULO")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's':
                print("Você votou Nulo")
                quant_votos_nulos_stranger_things = quant_votos_nulos_stranger_things + 1  
                break

# Quantidade de votos nas categoria do Homem Aranha
quant_votos_tobey  = 0
quant_votos_andrew = 0
quant_votos_tom = 0
quant_votos_brancos_homem_aranha = 0
quant_votos_nulos_homem_aranha = 0

def votacao_homem_aranha():
    global quant_votos_tobey, quant_votos_andrew, quant_votos_tom, quant_votos_brancos_homem_aranha, quant_votos_nulos_homem_aranha
    print("🕷️ HOMEM-ARANHA")
    print("Qual personagem você prefere? 🔎")
    print("11 - Tobey Maguire 🕷️")
    print("22 - Andrew Garfield 🕸️")
    print("33 - Tom Holland 🕷️")
    print("0 - Voto em Branco ⚪")
    print("Qualquer outro Número - Voto Nulo")
    print("")
    
    while True:
        escolha = int(input("Insira o número do candidato que você escolheu: "))
        if escolha == 11:
            print("Você apertou para votar em 11 - Tobey Maguire 🕷️")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 11 - Tobey Maguire 🕷️")
                quant_votos_tobey  = quant_votos_tobey  + 1
                break
        elif escolha == 22:
            print("Você apertou para votar em 22 - Andrew Garfield 🕸️")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 22 - Andrew Garfield 🕸️")
                quant_votos_andrew = quant_votos_andrew + 1
                break
        elif escolha == 33:
            print("Você apertou para votar em 33 - Tom Holland 🕷️")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 33 - Tom Holland 🕷️")
                quant_votos_tom = quant_votos_tom + 1 
                break
        elif escolha == 0:
            print("Você apertou para votar em Branco ⚪")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em Branco")
                quant_votos_brancos_homem_aranha = quant_votos_brancos_homem_aranha + 1
                break
        else:
            print("Você apertou para votar NULO")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's':
                print("Você votou Nulo")
                quant_votos_nulos_homem_aranha = quant_votos_nulos_homem_aranha + 1  
                break

# Quantidade de votos nas categoria das Rapunzel
quant_votos_rapunzel = 0
quant_votos_pascal = 0
quant_votos_flyn = 0
quant_votos_brancos_rapunzel = 0
quant_votos_nulos_rapunzel = 0

def votacao_Rapunzel():
    global quant_votos_rapunzel, quant_votos_pascal, quant_votos_flyn, quant_votos_brancos_rapunzel, quant_votos_nulos_rapunzel
    print("Rapunzel💜 ")
    print("Qual personagem de Enrolados você prefere? 💜")
    print("111 - Rapunzel💜")
    print("222 - Pascal🦎")
    print("333 - Flynn Rider🗡️ ")
    print("0 - Voto em Branco ⚪")
    print("Qualquer outro Número - Voto Nulo")
    print("")

    while True:
        escolha = int(input("Insira o número do candidato que você escolheu: "))
        if escolha == 111:
            print("Você apertou para votar em 111  Rapunzel💜")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 111  Rapunzel💜")
                quant_votos_rapunzel = quant_votos_rapunzel + 1
                break
        elif escolha == 222:
            print("Você apertou para votar em 222 - Pascal🦎")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 222 - Pascal🦎")
                quant_votos_pascal = quant_votos_pascal + 1
                break
        elif escolha == 333:
            print("Você apertou para votar em 333 - Flynn Rider🗡️ ")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 333 - Flynn Rider🗡️ ")
                quant_votos_flyn = quant_votos_flyn + 1 
                break
        elif escolha == 0:
            print("Você apertou para votar em Branco ⚪")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em Branco")
                quant_votos_brancos_rapunzel = quant_votos_brancos_rapunzel + 1
                break
        else:
            print("Você apertou para votar NULO")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's':
                print("Você votou Nulo")
                quant_votos_nulos_rapunzel = quant_votos_nulos_rapunzel + 1  
                break

# Quantidade de votos nas categoria do filme Rapunzel, mas relacionado com quem o usuário gostaria de ter como melhor amigo
quant_votos_maximus1 = 0
quant_votos_pascal1 = 0
quant_votos_flyn1= 0
quant_votos_brancos_Maximus1 = 0
quant_votos_nulos_Maximus1 = 0

def votacao_Maximus():
    global quant_votos_maximus1, quant_votos_pascal1, quant_votos_flyn1, quant_votos_brancos_Maximus1, quant_votos_nulos_Maximus1
    print("Rapunzel - Melhor Amigo 💜 ")
    print("Quem você escolheria para ser seu melhor amigo? 💜")
    print("111 - Maximus💜")
    print("222 - Pascal🦎")
    print("333 - Flynn Rider🗡️ ")
    print("0 - Voto em Branco ⚪")
    print("Qualquer outro Número - Voto Nulo")
    print("")

    while True:
        escolha = int(input("Insira o número do candidato que você escolheu: "))
        if escolha == 111:
            print("Você apertou para votar em 111  Maximus💜")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 111  Maximus💜")
                quant_votos_maximus1 = quant_votos_maximus1 + 1
                break
        elif escolha == 222:
            print("Você apertou para votar em 222 - Pascal🦎")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 222 - Pascal🦎")
                quant_votos_pascal1 = quant_votos_pascal1 + 1
                break
        elif escolha == 333:
            print("Você apertou para votar em 333 - Flynn Rider🗡️ ")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em 333 - Flynn Rider🗡️ ")
                quant_votos_flyn1= quant_votos_flyn1+ 1 
                break
        elif escolha == 0:
            print("Você apertou para votar em Branco ⚪")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's': 
                print("Você votou em Branco")
                quant_votos_brancos_Maximus1 = quant_votos_brancos_Maximus1 + 1
                break
        else:
            print("Você apertou para votar NULO")
            confirmacao = input("Confirme o seu voto: S - Sim     /     N - para Não: ")
            if confirmacao == 'S' or confirmacao == 's':
                print("Você votou Nulo")
                quant_votos_nulos_Maximus1 = quant_votos_nulos_Maximus1 + 1  
                break

# Imprime os votos, os mostra em quantidade e em porcentagem
def imprimir_votos():

    #Organizar a lista de cada uma dos candidatos e seus votos, em sua respectiva categoria
    lista_votacao_meninas_malvadas = [
        {"candidato": " Regina George 👑", "votos": quant_votos_regina},
        {"candidato": " Cady Heron 💕", "votos": quant_votos_cady},
        {"candidato": " Gretchen Wieners 💄", "votos": quant_votos_gretchen},
        {"candidato": " Voto em Branco ⚪", "votos": quant_votos_brancos_meninas_malvadas},
        {"candidato": " Voto Nulo", "votos": quant_votos_nulos_meninas_malvadas}
    ]

    lista_votacao_o_mentalista = [
        {"candidato": " Patrick Jane 🖤", "votos": quant_votos_patrick},
        {"candidato": " Teresa Lisbon 👮‍♀️", "votos": quant_votos_teresa},
        {"candidato": " Kimball Cho 💼", "votos": quant_votos_cho},  
        {"candidato": " Voto em Branco ⚪", "votos": quant_votos_brancos_mentalista}, 
        {"candidato": " Voto Nulo", "votos": quant_votos_nulos_mentalista}
    ]

    lista_votacao_stranger_things = [
        {"candidato": " Eleven 🧇 ", "votos": quant_votos_eleven},
        {"candidato": " Eddie Munson 🎸 ", "votos": quant_votos_eddie},
        {"candidato": " Steve Harrington 🧢", "votos": quant_votos_steve},  
        {"candidato": " Voto em Branco ⚪", "votos": quant_votos_brancos_stranger_things}, 
        {"candidato": " Voto Nulo", "votos": quant_votos_nulos_stranger_things}
    ] 

    lista_votacao_homem_aranha = [
        {"candidato": " Tobey Maguire 🕷️ ", "votos": quant_votos_tobey},
        {"candidato": " Andrew Garfield 🕸️ ", "votos": quant_votos_andrew},
        {"candidato": " Tom Holland 🕷️", "votos": quant_votos_tom},  
        {"candidato": " Voto em Branco ⚪", "votos": quant_votos_brancos_homem_aranha}, 
        {"candidato": " Voto Nulo", "votos": quant_votos_nulos_homem_aranha}
    ] 

    lista_votacao_rapunzel = [
        {"candidato": " Rapunzel💜 ", "votos": quant_votos_rapunzel},
        {"candidato": " Pascal🦎 ", "votos": quant_votos_pascal},
        {"candidato": " Flynn Rider🗡️", "votos": quant_votos_flyn},  
        {"candidato": " Voto em Branco ⚪", "votos": quant_votos_brancos_rapunzel}, 
        {"candidato": " Voto Nulo", "votos": quant_votos_nulos_rapunzel}
    ] 

    lista_votacao_maximus = [
        {"candidato": " Maximus💜 ", "votos": quant_votos_maximus1},
        {"candidato": " Pascal🦎 ", "votos": quant_votos_pascal1},
        {"candidato": " Flynn Rider🗡️", "votos": quant_votos_flyn1},  
        {"candidato": " Voto em Branco ⚪", "votos": quant_votos_brancos_Maximus1}, 
        {"candidato": " Voto Nulo", "votos": quant_votos_nulos_Maximus1}
    ] 

    os.system("cls")
    # Imprimir lista de votos da categoria Meninas Malvadas
    print("Quantidade de votos para a categoria 💗 Meninas Malvadas")
    total_votos = sum(item["votos"] for item in lista_votacao_meninas_malvadas)
    for item in lista_votacao_meninas_malvadas:
        porcentagem = (item["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{item['candidato']} = {item['votos']} ({porcentagem:.1f}%)")
    print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")

    # Imprimir lista de votos da categoria Mentalista
    print("Quantidade de votos para a categoria 🧠 O MENTALISTA")
    total_votos = sum(item["votos"] for item in lista_votacao_o_mentalista)
    for item in lista_votacao_o_mentalista:
        porcentagem = (item["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{item['candidato']} = {item['votos']} ({porcentagem:.1f}%)")
    print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")

    # Imprimir lista de votos da categoria 👾 STRANGER THINGS
    print("Quantidade de votos para a categoria 👾 STRANGER THINGS")
    total_votos = sum(item["votos"] for item in lista_votacao_stranger_things)
    for item in lista_votacao_stranger_things:
        porcentagem = (item["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{item['candidato']} = {item['votos']} ({porcentagem:.1f}%)")
    print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")

    # Imprimir lista de votos da categoria 🕷️ HOMEM-ARANHA
    print("Quantidade de votos para a categoria 🕷️ HOMEM-ARANHA")
    total_votos = sum(item["votos"] for item in lista_votacao_homem_aranha)
    for item in lista_votacao_homem_aranha:
        porcentagem = (item["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{item['candidato']} = {item['votos']} ({porcentagem:.1f}%)")
    print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")

    # Imprimir lista de votos da categoria Rapunzel💜
    print("Quantidade de votos para a categoria Rapunzel💜")
    total_votos = sum(item["votos"] for item in lista_votacao_rapunzel)
    for item in lista_votacao_rapunzel:
        porcentagem = (item["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{item['candidato']} = {item['votos']} ({porcentagem:.1f}%)")
    print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")

    # Imprimir lista de votos da categoria Maximus💜
    print("Quantidade de votos para a categoria Rapunzel - Melhor Amigo 💜")
    total_votos = sum(item["votos"] for item in lista_votacao_maximus)
    for item in lista_votacao_maximus:
        porcentagem = (item["votos"] / total_votos) * 100 if total_votos > 0 else 0
        print(f"{item['candidato']} = {item['votos']} ({porcentagem:.1f}%)")
    print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡")

while True:
    match estado: 
        case "menu": 
            os.system("cls")
            nomeloja()
            print("")
            print("♡₊˚ Bem-vindo à sua urna de favoritos! 🎬 Vote no seu personagem preferido <3")
            print("")
            print("1. Realizar Votação 🎀")
            print("")
            estado = input("Digite qual menu você quer acessar: ")

        case "1":
            os.system("cls")
            print("🗳️ Você está iniciando sua votação: \n")
            votacao_meninas_malvadas()
            print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")
            votacao_mentalista()
            print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")
            votacao_stranger_things()
            print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")
            votacao_homem_aranha()
            print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")
            votacao_Rapunzel()
            print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")
            votacao_Maximus()
            print("♡₊˚・₊✧・₊˚・₊✧ 🦢 ✧₊・₊˚・₊✧・₊˚♡\n")
            input("Aperte ENTER para voltar ao menu...")
            estado = "menu"

        # Esse case não aparece no menu para que os usuários não possam saber o número de votos
        # O administrador deve observar o que precisa ser apertado para que se possa ver a lsita de votaçao
        case  "Votos" | "Voto" | "voto" | "votos" | "V" | "v" :
            imprimir_votos()
            input("\nAperte ENTER para voltar ao menu...")
            estado = "menu"
        
        case "0":
            os.system("cls")
            print("Você saiu do programa!")
            break
            
        case _:
            print("Opção Inválida.")
            input("Aperte ENTER para tentar novamente...")
            estado = "menu"