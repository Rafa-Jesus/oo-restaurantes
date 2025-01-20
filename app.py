from modelos.restaurante import Restaurante

restauranta_pizzaria = Restaurante('Pizza Express', 'Italiana')
restauranta_pizzaria.receber_avaliacao('Rafa', 9)
restauranta_pizzaria.receber_avaliacao('Sofi', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()