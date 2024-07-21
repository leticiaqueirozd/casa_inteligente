from transitions import Machine
from src.dispositivo import Dispositivo

class Luz(Dispositivo):
    states = ['desligada', 'ligada']

    def __init__(self, nome):
        self.nome = nome
        self.state = 'desligada'
        self.machine = Machine(model=self, states=Luz.states, initial='desligada')
        self.machine.add_transition(trigger='start_ligar', source='desligada', dest='ligada')
        self.machine.add_transition(trigger='start_desligar', source='ligada', dest='desligada')

    def get_status(self):
        return f"A luz '{self.nome}' está {self.state}"

    def ligar(self):
        self.start_ligar()

    def desligar(self):
        self.start_desligar()
