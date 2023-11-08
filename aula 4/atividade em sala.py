from datetime import datetime

def dia_da_semana(data):
    # converte a string para datetime
    data = datetime.strptime(data, '%d/%m/%Y')
    # formata a data para obter o nome do dia da semana
    return data.strftime('%A')

# exemplo de uso da função
data = '02/11/2023'
print(dia_da_semana(data)) 