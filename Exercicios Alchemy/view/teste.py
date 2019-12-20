import sys
sys.path.append('C:/Users/900225/Desktop/AulasPythonClt2/Aula13/estrutura')

from model.papel import Papel
from model.cotacao_diaria import CotacaoDiaria
from dao.papel_dao import PapelDao
from dao.tipo_dao import TipoPapelDao
from dao.tipo_rendimento_dao import TipoRendimentoDao
from dao.rendimento_dao import RendimentoDao
from dao.cotacao_diaria_dao import CotacaoDiariaDao

dao = PapelDao()
dao_tipo = TipoPapelDao()

# papel = Papel()
# papel.codigo = 'DISB34'
# papel.descricao = 'Disney'
# papel.tipo_id = 5
# dao.insert(papel)

# papel = Papel()
# papel.codigo = 'Teste2'
# papel.descricao = 'testes2'
# papel.tipo_id = 2
# papel.id=10

#dao.insert(papel)
#dao.update(papel)
# dao.delete(10)
# for p in dao.list_all():
#     print(f'{p}')

# for tp in dao_tipo.list_all():
#     print(f'\t{tp}')



#--------------- Tipo Rendimento
# dao_tr = TipoRendimentoDao()
# for tr in dao_tr.list_all():
#     print(f'{tr}')

#---------------  Rendimento
# dao_r = RendimentoDao()
# for r in dao_r.list_all():
#     print(f'{r}')

#---------------  Cotacao Diaria
dao_cd = CotacaoDiariaDao()
# for cd in dao_cd.list_all():
#     print(f'{cd}')

# cotacao = CotacaoDiaria()
# cotacao.papel_id =22
# cotacao.valor_abertura = 19.60
# cotacao.valor_fechamento = 19.71
# cotacao.data = '2019-12-19'

# dao_cd.insert(cotacao)

for cd in dao_cd.list_lower_lpa():
    print(f'{cd.papel.codigo} - {cd.papel.descricao} - {cd.valor_fechamento:.2f}  - {cd.lpa:.2f} - {cd.pl:.2f}')