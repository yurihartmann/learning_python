# Organize a lista de produtos de um supermercado
# Utilize classes para converter as listas em objetos
# Salve o dados em uma tabela no banco de dados
# Separar a aplicação em camadas
# Listar produtos e seus respectivos preços por categoria, de acordo com a categoria selecionada pelo usuario

# para exemplificar, 
# o preço da: fruta   -> abacaxi ->  2.56
# o preço da: verdura -> almerão ->  3.25

from produto import Produto

from produto_dao import ProdutoDao

lista = [
            ['frutas','verduras','legumes','preço'],
            ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
            ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha','couve'],
            ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
            [ 
                [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
                [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
            ]
        ]


produto_dao = ProdutoDao()

# MONTANDO FRUTAS
for i in range(len(lista[1])):
    nome_fruta = lista[1][i]
    preco = lista[4][0][i]
    produto_dao.inserir(Produto(nome_fruta, 'fruta', preco))


# MONTANDO VERDURAS
for i in range(len(lista[2])):
    nome_fruta = lista[2][i]
    preco = lista[4][1][i]
    produto_dao.inserir(Produto(nome_fruta, 'verdura', preco))

# MONTANDO LEGUMES
for i in range(len(lista[3])):
    nome_fruta = lista[3][i]
    preco = lista[4][2][i]
    produto_dao.inserir(Produto(nome_fruta, 'legume', preco))
    

