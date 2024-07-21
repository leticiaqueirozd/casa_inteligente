class Observer:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"{self.nome} recebeu notificação: {mensagem}")
