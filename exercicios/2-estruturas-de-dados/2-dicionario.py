pessoa = {'nome':'Crislaine', 
          'idade':46, 
          'ano_formatura':2010, 
          'linguagens_programacao':['python', 'r', 'javascript', 'ruby'], 
          'brasileira':True, 
          'hobby':['nadar', 'ler', 'pedalar'], 
          'animal_estimacao':False}

# Imprima na tela o valor equivalente a chave "hobby"
print(pessoa['hobby'])

# Imprima na tela uma lista apenas com os valores do dicionário
print(pessoa.values())

# Imprima na tela uma lista apenas com as chaves do dicionário
list(pessoa.keys())
print(list(pessoa.keys()))
# Insira um novo par chave-valor no dicionário
pessoa['ano_Nascimento:'] = 1997
print(pessoa)

pessoa.pop('idade')
print(pessoa)