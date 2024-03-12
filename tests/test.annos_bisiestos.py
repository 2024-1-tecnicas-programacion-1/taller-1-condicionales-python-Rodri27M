import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.annos_bisiestos import evaluar
class TestAnnosBisiestos(unittest.TestCase):
    
    def test_1988(self):
        valor_esperado = "1988 es bisiesto"
        valor_actual = evaluar(1988)
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
    

    def test_1700(self):
        valor_esperado = "1700 no es bisiesto"
        valor_actual = evaluar(1700)
        self.assertEqual(valor_esperado, valor_actual)

    def test_2400(self):
        valor_esperado = "2400 es bisiesto"
        valor_actual = evaluar(2400)
        self.assertEqual(valor_esperado, valor_actual)
if __name__ == '__main__':
    unittest.main()
