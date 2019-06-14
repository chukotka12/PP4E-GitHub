"""
пример использования unittest

"""
import unittest, sys


# определение декоратора пропуска теста, если отсутствует аттрибут в объекте
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip('{!r} doesn\'t have {!r}'.format(obj, attr))

# варианты пропуска теста
class MyTestCase(unittest.TestCase):
    @unittest.skip('demonstating skipping')
    def test_nothing(self):
        self.fail('should\'t happen')

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # test that work for only a certain version of the lib
        pass

    @unittest.skipUnless(sys.platform.startswith('win'),
                         'requred Windows')
    def test_windows_support(self):
        # windows specific testing code
        pass


# вариант пропуска класса
@unittest.skip('showing class skipping')
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
