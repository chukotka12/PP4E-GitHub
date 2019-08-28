# обработчики: перезагружаются перед каждым вызовом
def message1():
    print('spamSpamSPAM')


def message2(self):
    print('Ni! ' * 2)
    self.method1()  # обращение к экземпляру Hello
