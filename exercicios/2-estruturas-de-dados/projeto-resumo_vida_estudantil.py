# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {

}

estudante['nome'] = input('Qual o nome do aluno? \n')
estudante['anoLinkedin'] = int(input('Em qual ano conheceu o Linkedn ? \n'))
estudante['anoAtual'] = int(input('Qual o ano atual ? \n'))
cursos = input('Qual os cursos que você já realizou no Linkedn Learning ?\n')
estudante['cursos'] = cursos.split(', ')

totalAnos = estudante['anoAtual'] - estudante ['anoLinkedin']
totalCursos = len(estudante['cursos'])

print(f"O {estudante['nome']} conheceu o Linkedn no ano de {estudante['anoLinkedin']} e já está usando a plataforma a {totalAnos} anos, e desde esse tempo já realizou {totalCursos} cursos")
print(f"Sendo o primeiro curso {estudante['cursos'] [0]} e o ultimo curso {estudante['cursos'][-1]}")