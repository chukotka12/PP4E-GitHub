# пример использования unittest
import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEquals('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # проверка что s.split не работает, если
        # разделитель не строка
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
