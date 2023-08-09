import random
import loja 
import batalha

opcoes_dificuldade = {
    "1": {"chance_rainha": 0.2},
    "2": {"chance_rainha": 0.4},
    "3": {"chance_rainha": 0.6}
}

print("Escolha a dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")
dificuldade_escolhida = input("Escolha uma opção: ")

if dificuldade_escolhida not in opcoes_dificuldade:
    print("Opção inválida! O jogo foi encerrado.")
else:
    dificuldade = opcoes_dificuldade[dificuldade_escolhida]
    
    personagem = {
        "nome": "Jô Soares",
        "vida": 100,
        "dinheiro": 1000,
    }

    guardas = [
        {"nome": "Thorne", "titulo": "O Mestre da Trapaça", "vida": 50},
        {"nome": "Lorde Mortimer", "titulo": "O Perseguidor", "vida": 90},
        {"nome": "Vladrik", "titulo": "(Irmão de Petrick), O Carniceiro Implacável", "vida": 120},
        {"nome": "Petrick", "titulo": "(Irmão de Vladrik), O Vegano Implacável", "vida": 150}
    ]

    venceu_guardas = True

    for i, guarda in enumerate(guardas, 4):
        last_choice = None
        while True:
            print("Você tem duas opções:")
            print("[1] - Ir para a loja")
            print("[2] - Enfrentar o próximo guarda")
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                print("Você foi para a loja e recarregou suas energias.")
                personagem["vida"] = 100
                loja.mostrar_loja(personagem)
                
                 
            elif escolha == "2":
                result = batalha.batalhar(personagem, guarda)
                if not result:
                    print("Fim de jogo! Tente novamente.")
                    venceu_guardas = False 
                    break  
                else:
                    break  
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
                if last_choice is not None:
                    escolha = last_choice  
                    break  
                last_choice = escolha 

if venceu_guardas:
    print("Parabéns! Você derrotou todos os guardas e está pronto para enfrentar o Rei!")

    rei = {
        "nome": "Rei Malvado",
        "titulo": "O Terrível",
        "vida": 250
    }

    print("Agora é hora de enfrentar o Rei!")

    while True:
        print("Você tem duas opções:")
        print("[1] - Enfrentar o Rei")
        print("[2] - Ir para a loja")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            result_rei = batalha.batalhar_rei(personagem, rei)
            if result_rei:
                print("Você venceu o Rei! Continue enfrentando a Rainha.")
            else:
                print("Você foi derrotado pelo Rei. Tente novamente!")
            break
        elif escolha == "2":
            print("Você foi para a loja e recarregou suas energias.")
            personagem["vida"] = 100
            loja.mostrar_loja(personagem)  
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

    if random.random() < dificuldade["chance_rainha"]:
        print("Você teve coragem de enfrentar a terrível Rainha Barrenta!")
        rainha = {
            "nome": "Rainha Barrenta",
            "titulo": "A Lamacenta",
            "vida": 200
        }
        
        last_choice = None 
        while True:
            print("Você tem duas opções:")
            print("[1] - Enfrentar a Rainha")
            print("[2] - Não enfrentar a Rainha")
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                result_rainha = batalha.batalhar_rainha(personagem, rainha)
                if result_rainha:
                    print("Parabéns! Você derrotou a Rainha Barrenta e salvou o reino novamente!")
                else:
                    print("Infelizmente, você foi derrotado pela Rainha Barrenta. Tente novamente!")
                break  
            elif escolha == "2":
                print("Você optou por não enfrentar a terrível Rainha Barrenta. Fim de jogo!")
                break 
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
                if last_choice is not None:
                    escolha = last_choice  
                    break 
                last_choice = escolha
            
    else:
        print("Você optou por não enfrentar a terrível Rainha Barrenta. Fim de jogo!")

