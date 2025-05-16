# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome = input('Qual é o nome do aluno ? \n')
totalDias = input('Quantos dias ? \n')
totalHoras = input('Quantas horas você se dedica ?\n')
curso = input('Qual o curso ?\n')

totalDias = int(totalDias)  #conversão de String para inteiro
totalHoras = int(totalHoras) #conversão de String para inteiro

print(f'Olá {nome}, você costuma estudar {totalDias} dias por semana durante {totalHoras} horas diárias,isso significa que você estuda em média {totalHoras * totalDias} horas por semana para o curso de {curso}')


