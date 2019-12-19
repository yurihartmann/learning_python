from pessoa import Pessoa

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
        ]

# 1 - Usando as 2 listas, fazer uma função que crie retorne uma lista com objetos de classe  Pessoa
# com os dados das pessoas com idade maior ou igual a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo os dados da classe para cada pessoa criada 
# (usando o f-string)]

def pessoa_maior_de_idade(pessoas: list):
    retorno = []
    for i in range(len(pessoas[0])):

        if int(pessoas[3][i]) >= 18:
            p = Pessoa(pessoas[0][i], pessoas[1][i], pessoas[2][i], pessoas[3][i])
            retorno.append(p)
    return retorno

alo = pessoa_maior_de_idade(pess)

for p in alo:
    print(f"Nome: {p.nome} - Telefone: {p.tel} - E-mail: {p.email} - Idade: {p.idade} anos")



        

