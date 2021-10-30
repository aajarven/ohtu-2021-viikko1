import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_vaikuta(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ylitaytto_ei_mahdollista(self):
        self.varasto.lisaa_varastoon(99)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_ei_palauta_tavaraa(self):
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_tyhjan_varaston_str(self):
        self.assertEqual(str(self.varasto),
                         "saldo = 0, vielä tilaa 10")


class TestEsitaytettyVarasto(unittest.TestCase):

    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(8)

    def test_vajaan_varaston_str(self):
        self.assertEqual(str(self.varasto),
                         "saldo = 8, vielä tilaa 2")

    def test_negatiivinen_otto_ei_vahenna_saldoa(self):
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_varasto_palauttaa_korkeintaan_saldon_verran_tavaraa(self):
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)


class TestNegatiivisenTilavuudenVarasto(unittest.TestCase):

    def setUp(self):
        self.varasto = Varasto(-10)

    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        self.assertEqual(self.varasto.tilavuus, 0)


class TestNegatiivisenAlkusaldonVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, -5)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)
