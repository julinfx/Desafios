'''
Criar um programa que gera 3 listas com as necessidaes abaixo:

Lista1 = 'Funcionario que tem carro e trabalhando a noite
lista2 = funcionarios que tem carro e trabalham durante o dia
lista3 = funcionarios que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro','Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice','Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

set_funcionarios = set(funcionarios)
set_dia = set(turno_dia)
set_noite = set(turno_noite)
set_carro = set(tem_carro)

list1 = set_carro & set_noite
list2 = set_carro & set_dia
list3 = set_funcionarios - set_carro

print(f'Funcionários que tem carro e trabalham a noite {list1}')
print(f'Funcionários que tem carro e trabalham de dia {list2}')
print(f'Funcionários que não tem carro {list3}')
