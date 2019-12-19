from produto_dao import ProdutoDao
from produto import Produto

produto_dao = ProdutoDao()


while True:
    print(" Escolha um tipo para listar:")
    print(" 1 - Fruta")
    print(" 2 - Verdura")
    print(" 3 - Legume")

    id_tipo = input()

    produtos = produto_dao.listar_by_tipo_id(id_tipo)

    print(f" =-=-==-=-= {produtos[0].tipo.upper()} =-=-==-=-=")
    for p in produtos:
        print(f"Nome: {p.nome} - Preco: R$ {p.valor:.2f}")

    print("=-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-=")
