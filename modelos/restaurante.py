from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas características'''

    restaurantes = []

    def __init__(self, nome, categoria):
        '''Inicializa uma instância de Restaurante
        
        Parâmetros:
        - Nome (str): nome do restaurante
        - Categoria (str): categoria do restaurante'''

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Cria uma representação em string do restaurante'''
        return f'{self._nome} | {self._categoria} | {self._ativo}'

    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes disponíveis'''
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)} | {str(restaurante.media_avaliacoes).ljust(15)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        '''Retorna um símbolo de acordo com o status do restaurante'''
        return '✔️' if self._ativo else '✖️'
    
    def receber_avaliacao(self, cliente, nota):
        '''Registra uma avaliação para o restaurante'''
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações dos restaurantes'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        total_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / total_de_notas, 1)
        return media

    def alternar_status(self):
        '''Altera o status do restaurante'''
        self._ativo = not self._ativo