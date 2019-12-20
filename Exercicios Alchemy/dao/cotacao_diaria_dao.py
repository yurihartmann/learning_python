from dao.base_dao import BaseDao
from model.cotacao_diaria import CotacaoDiaria

class CotacaoDiariaDao(BaseDao):
    def __init__(self):
        self.model = CotacaoDiaria
        super().__init__(self.model)
    
    def list_lower_lpa(self):
        dados = self.session.query(self.model).order_by(self.model.lpa).all()

        for d in dados:
            d.pl = d.valor_fechamento / d.lpa
        
        return sorted(dados, key = CotacaoDiaria.get_pl)