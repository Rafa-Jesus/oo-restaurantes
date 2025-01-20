from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)} | {str(restaurante.media_avaliacoes).ljust(15)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return '✔️' if self._ativo else '✖️'
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        total_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / total_de_notas, 1)
        return media

    def alternar_status(self):
        self._ativo = not self._ativo