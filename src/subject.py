class Subject:
    def __init__(self):
        self.observers = []

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def notificar_observers(self, mensagem):
        for observer in self.observers:
            observer.atualizar(mensagem)