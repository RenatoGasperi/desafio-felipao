def pontuacao():
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))
    
    saldo = vitorias-derrotas
    return saldo

def rank(x):
    if x < 10:
        x = "Ferro"
    elif x > 10 and x < 21:
        x = "Bronze"
    elif x > 20 and x < 51:
        x = "Prata"
    elif x > 50 and x < 81:
        x = "Ouro"
    elif x > 80 and x < 91:
        x = "Diamante"
    elif x > 90 and x < 101:
        x = "Lendario"
    elif x > 101:
        x = "Imortal"
    else:
        x = "0"
    return x

saldoVitorias = pontuacao()
nivel = rank(saldoVitorias)



if nivel == "Ferro":
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")
        
elif nivel == "Bronze":
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")

elif nivel == "Prata":
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")
    
elif nivel == "Ouro":
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")

elif nivel == "Diamante":
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**") 
    
elif nivel == "Lendario":
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")
    
elif nivel == "Imortal":
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")
    
else:
    print("Valor errado")   
