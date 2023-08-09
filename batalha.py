import random

def batalhar(personagem, inimigo):
    print(f"Você está enfrentando o {inimigo['nome']} - {inimigo['titulo']}")
   
    while personagem["vida"] > 0 and inimigo["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida do {inimigo['nome']}: {inimigo['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        input("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        print("[3] - Usar poção de sono")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            if personagem.get('espada', False):  
                player_attack_damage = random.randint(15, 25) 
            else:
                player_attack_damage = random.randint(5, 15)  
           
            player_attack_damage = random.randint(5, 15)
            
            is_critical = random.random() < 0.2 
            if is_critical:
                player_attack_damage *= 2  
                print("DANO CRÍTICO!")
            inimigo["vida"] -= player_attack_damage
            print(f"{personagem['nome']} ataca {inimigo['nome']} e causa {player_attack_damage} de dano.")
            
       
            if random.random() < 0.05:  
                moedas_encontradas = random.randint(20, 50)
                print(f"Você encontrou um baú de moedas! Ganhou {moedas_encontradas} moedas!")
                personagem["dinheiro"] += moedas_encontradas
        elif escolha == "2":
            print("Você fugiu da batalha!")
            return False
        elif escolha == "3":
            usar_pocao_de_sono(personagem, inimigo)  
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if inimigo["vida"] <= 0:
            print(f"Você derrotou o {inimigo['nome']}!")
            moedas_ganhas = random.randint(10, 20)  
            print(f"Você ganhou {moedas_ganhas} moedas!")
            personagem["dinheiro"] += moedas_ganhas
            return True
       
     
        if random.random() < 0.3: 
            print(f"{inimigo['nome']} errou o ataque!")
        else:
            enemy_attack_damage = random.randint(8, 12)
            personagem["vida"] -= enemy_attack_damage
            print(f"{inimigo['nome']} ataca {personagem['nome']} e causa {enemy_attack_damage} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado!")
            return False

def batalhar_rei(personagem, rei):
    print(f"Você está enfrentando o Rei {rei['nome']} - {rei['titulo']}")
   
    while personagem["vida"] > 0 and rei["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida do Rei {rei['nome']}: {rei['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        input("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        print("[3] - Usar poção de sono")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            if personagem.get('espada', False):
                player_attack_damage = random.randint(15, 25) 
            else:
                player_attack_damage = random.randint(5, 15)  
           
            is_critical = random.random() < 0.2  
            if is_critical:
                player_attack_damage *= 2 
                print("DANO CRÍTICO!")
            rei["vida"] -= player_attack_damage
            print(f"{personagem['nome']} ataca o Rei {rei['nome']} e causa {player_attack_damage} de dano.")
        elif escolha == 2:
            print("Você fugiu da batalha!")
            return False
        elif escolha == "3":
            usar_pocao_de_sono(personagem, rei) 
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if rei["vida"] <= 0:
            print(f"Você derrotou o Rei {rei['nome']}!")
            print("Você venceu o jogo! Parabéns!")
            return True
       

        rei_attack_damage = random.randint(50, 100)
        personagem["vida"] -= rei_attack_damage
        print(f"O Rei {rei['nome']} ataca {personagem['nome']} e causa {rei_attack_damage} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado pelo Rei!")
            return False

def batalhar_rainha(personagem, rainha):
    print(f"Você está enfrentando a Rainha {rainha['nome']} - {rainha['titulo']}")
   
    while personagem["vida"] > 0 and rainha["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida da Rainha {rainha['nome']}: {rainha['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        input("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        print("[3] - Usar poção de sono")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == 1:
            if personagem.get('espada', False):  
                player_attack_damage = random.randint(15, 25) 
            else:
                player_attack_damage = random.randint(5, 15) 
          
            is_critical = random.random() < 0.2 
            if is_critical:
                player_attack_damage *= 2 
                print("DANO CRÍTICO!")
            rainha["vida"] -= player_attack_damage
            print(f"{personagem['nome']} ataca a Rainha {rainha['nome']} e causa {player_attack_damage} de dano.")
        elif escolha == "2":
            print("Você fugiu da batalha!")
            return False
        elif escolha == "3":
            usar_pocao_de_sono(personagem, rainha)  
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if rainha["vida"] <= 0:
            print(f"Você derrotou a Rainha {rainha['nome']}!")
            print("Você venceu o jogo! Parabéns!")
            return True
       
     
        rainha_attack_damage = random.randint(40, 80)
        personagem["vida"] -= rainha_attack_damage
        print(f"A Rainha {rainha['nome']} ataca {personagem['nome']} e causa {rainha_attack_damage} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado pela Rainha!")
            return False
        
def usar_pocao_de_sono(personagem, inimigo):
    if personagem.get('poção_de_sono', False):
        print("Você usou a Poção de Sono e colocou o adversário para dormir!")
        inimigo['vida'] = 0
        del personagem['poção_de_sono'] 
    else:
        print("Você não tem uma Poção de Sono para usar.")