def producao_por_maquina(producao, produto, maquina):
    # Subtrai o -1 dos numeros de produto e maquina pois ao acessar a Matriz o indice começa em 0, e para reparar isso, é so subtrair 1, que iremos igualar e ter o valor correto.
    return producao[produto - 1][maquina - 1]


# Aqui eu defini a matriz que recebi no Desafio da semana 1
producao = [[560, 360, 380, 0], [340, 450, 420, 80], [280, 270, 210, 380]]

# Aqui fiz as entradas de input para o usuário selecionar qual máquina e produto ele gostaria de ter a produção.


# Utilizei um int para transformar os valor que antes estavam em string, o input para mandar ao terminal a pergunta e armazenei nas respectivas variaveis.
produto = int(input("Qual é o número do produto (1, 2 ou 3): "))


maquina = int(input("Qual é o número da máquina (1, 2, 3 ou 4): "))


# Aqui chamei a função que criei la em cima com os argumentos e chamei abaixo e coloquei o resultado na respectiva variavel
produzido = producao_por_maquina(producao, produto, maquina)


# Aqui fiz um print básico para dar a resposta para o usuário.
print(f"Unidades do produto {produto} produzidas pela máquina {maquina}: {produzido}")
