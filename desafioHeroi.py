nomeHeroi =  input("Digite o nome do Herói: ").upper()
xp = int(input("Digite a quantidade experiencia herói: "))

if xp > 0 and xp < 1001:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Ferro**")
        
elif xp > 1001 and xp < 2001:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Bronze**")

elif xp > 2001 and xp < 5001:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Prata**")
    
elif xp > 5001 and xp < 7001:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Ouro**")

elif xp > 7001 and xp < 8001:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Platina**")   
    
elif xp > 8001 and xp < 9001:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Ascendente**") 
    
elif xp > 9001 and xp < 10001:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Imortal**")
    
elif xp > 10000:
    print(f"O Herói de nome **{nomeHeroi}** está no nível de **Radiante**")
else:
    print("Valor errado")   
