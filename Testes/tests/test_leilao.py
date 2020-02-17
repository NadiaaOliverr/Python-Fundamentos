from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao

# Outro tipo de nomenclatura dem testes:
# test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self): #método padrão do unittest para criar algum cenário, ele é invocado antes de rodar os testes e ele é sempre executado novamente a cada teste, é feito de forma isolada
        #boa prática é deixar apenas todos os atributos que são usados em TODOS OS TESTES, pois, caso tenha 4 atributos e só use 1, pode deixar esta parte do código menos perfomática
        self.gui = Usuario('Gui', 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500.0)

        lance_do_yuri = Lance(yuri, 100.0)


        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_descrescente(self):

        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500.0)

            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini', 500.0)
        lance_do_vini = Lance(vini, 200.0)
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)


        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # Se o leilão não tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_esperado = 1
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(quantidade_de_lances_esperado, quantidade_de_lances_recebido)

    # Se o último usuário for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)

        lance_do_yuri = Lance(yuri, 200.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances_esperado = 2
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(quantidade_de_lances_esperado, quantidade_de_lances_recebido)
    # Se o último usuário for o mesmo, não deve permitir propor o lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)

