from transitions import Machine
from src.dispositivo import Dispositivo

class Termostato(Dispositivo):
    states = ['desligado', 'aquecendo', 'esfriando']

    def __init__(self, nome):
        self.nome = nome
        self.state = 'desligado'
        self.machine = Machine(model=self, states=Termostato.states, initial='desligado')
        self.machine.add_transition(trigger='start_aquecer', source='desligado', dest='aquecendo')
        self.machine.add_transition(trigger='start_esfriar', source='desligado', dest='esfriando')
        self.machine.add_transition(trigger='start_desligar', source=['aquecendo', 'esfriando'], dest='desligado')

    def get_status(self):
        return f"O termostato '{self.nome}' está {self.state}"

    def aquecer(self):
        self.start_aquecer()

    def esfriar(self):
        self.start_esfriar()

    def desligar(self):
        self.start_desligar()
