from transitions import Machine
from src.dispositivo import Dispositivo

class SistemaSeguranca(Dispositivo):
    states = ['desarmado', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa']

    def __init__(self, nome):
        self.nome = nome
        self.state = 'desarmado'
        self.machine = Machine(model=self, states=SistemaSeguranca.states, initial='desarmado')
        self.machine.add_transition(trigger='start_armar_com_gente', source='desarmado', dest='armado_com_gente_em_casa')
        self.machine.add_transition(trigger='start_armar_sem_gente', source='desarmado', dest='armado_sem_ninguem_em_casa')
        self.machine.add_transition(trigger='start_desarmar', source=['armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'], dest='desarmado')

    def get_status(self):
        return f"O sistema de segurança '{self.nome}' está {self.state}"

    def armar_com_gente_em_casa(self):
        self.start_armar_com_gente()

    def armar_sem_gente_em_casa(self):
        self.start_armar_sem_gente()

    def desarmar(self):
        self.start_desarmar()
