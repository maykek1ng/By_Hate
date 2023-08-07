def barganhar(personagem):
    return personagem

loja = [
    {"NomeEquipamento": "espada de pau", "valor": 30, "dano": 18},
    {"NomeEquipamento": "espada de ferro", "valor": 70, "dano": 30},
    {"NomeEquipamento": "espada de ruby", "valor": 200, "dano": 90},
    {"NomeEquipamento": "espada de lagrima do crocodilo do nilo albino dos olhos vermelhos", "valor": 500, "dano": 200},
    {"NomeEquipamento": "armadura de couro", "valor": 30, "hpAgregado": 20},
    {"NomeEquipamento": "armadura de ferro", "valor": 70, "hpAgregado": 50},
    {"NomeEquipamento": "armadura de diamante", "valor": 200, "hpAgregado": 90},
    {"NomeEquipamento": "armadura de adamantium", "valor": 500, "hpAgregado": 200}
]

def exibir_loja(loja):
    print("----- Loja RPG -----")
    for i, item in enumerate(loja, 1):
        print(f"{i}. {item['NomeEquipamento']} - Valor: {item['valor']}")

def comprar_item(personagem, item_index):
    item = loja[item_index]
    if 'dano' in item:
        personagem['dano'] = max(personagem['dano'], item['dano'])
    elif 'hpAgregado' in item:
        personagem['hp'] += item['hpAgregado']
    personagem['moedas'] -= item['valor']
    return personagem

personagem = {'moedas': 1000, 'dano': 10, 'hp': 100}

exibir_loja(loja)

while True:
    try:
        opcao = int(input("Escolha um item para comprar (0 para sair): "))
        if opcao == 0:
            break
        elif 1 <= opcao <= len(loja):
            item_index = opcao - 1
            item = loja[item_index]
            if personagem['moedas'] >= item['valor']:
                personagem = comprar_item(personagem, item_index)
                print("Compra realizada com sucesso!")
            else:
                print("Você não tem moedas suficientes para comprar esse item.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite um número válido.")

print(f"\nSeu personagem após as compras: {personagem}")