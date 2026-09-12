import unittest
from frete import calcular_frete

class TestFrete(unittest.TestCase):
    def test_valor_carrinho_invalido(self):
        # RB-05: IF price <= 0, THEN show the error 'Valor de carrinho inválido'
        with self.assertRaises(ValueError) as context:
            calcular_frete(0, "Norte")
        self.assertEqual(str(context.exception), "Valor de carrinho inválido")

        with self.assertRaises(ValueError) as context:
            calcular_frete(-50.0, "Sul")
        self.assertEqual(str(context.exception), "Valor de carrinho inválido")

    def test_norte_free_shipping_limit(self):
        # RB-01 & RF-02: Norte limit is 300.00
        # Equal to limit
        self.assertEqual(calcular_frete(300.00, "Norte"), 0.0)
        # Above limit
        self.assertEqual(calcular_frete(350.00, "Norte"), 0.0)

    def test_other_regions_free_shipping_limit(self):
        # RB-01 & RF-02: Other regions limit is 200.00
        # Equal to limit
        self.assertEqual(calcular_frete(200.00, "Sul"), 0.0)
        # Above limit
        self.assertEqual(calcular_frete(250.00, "Sudeste"), 0.0)

    def test_norte_below_limit_discount_rb02(self):
        # RB-02: IF shipping cost > 40.00, reduce price (shipping) by 10%
        # e.g., base shipping 50.00 -> 45.00
        self.assertAlmostEqual(calcular_frete(150.00, "Norte", 50.0), 45.0, places=2)

    def test_discount_rb03(self):
        # RB-03: IF shipping cost R$19.99 >= x >= R$29.99, reduce price by 50%
        # (interpreted as 19.99 <= shipping_cost <= 29.99)
        # Equal to lower bound
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 19.99), 10.00, places=2) # 19.99 * 0.5 = 9.995, rounded to 2 places is 10.00
        # Equal to upper bound
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 29.99), 15.00, places=2) # 29.99 * 0.5 = 14.995, rounded to 2 places is 15.00
        # In between
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 25.00), 12.50, places=2)

    def test_discount_rb04(self):
        # RB-04: IF shipping cost > R$10.00 x < R$19.99, reduce price by 10%
        # Just above 10.00
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 10.01), 9.01, places=2) # 10.01 * 0.9 = 9.009 -> 9.01
        # Just below 19.99
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 19.98), 17.98, places=2) # 19.98 * 0.9 = 17.982 -> 17.98
        # In between
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 15.00), 13.50, places=2)

    def test_no_discount_cases(self):
        # Below 10.00
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 9.00), 9.00, places=2)
        # Between 29.99 and 40.00 (e.g. 35.00)
        self.assertAlmostEqual(calcular_frete(100.00, "Sul", 35.00), 35.00, places=2)

if __name__ == '__main__':
    unittest.main()
