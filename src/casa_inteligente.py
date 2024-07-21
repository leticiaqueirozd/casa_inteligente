from functools import reduce
from meus_dispositivos.luz import Luz
from meus_dispositivos.sistema_seguranca import SistemaSeguranca
from meus_dispositivos.termostato import Termostato
from src.subject import Subject


class CasaInteligente(Subject):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CasaInteligente, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        super().__init__()
        self.dispositivos = []
        self.__initialized = True

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)
        self.notificar_observers(f"Dispositivo '{dispositivo.nome}' adicionado.")

    def remover_dispositivo(self, dispositivo):
        if dispositivo in self.dispositivos:
            self.dispositivos.remove(dispositivo)
            self.notificar_observers(f"Dispositivo '{dispositivo.nome}' removido.")
    
    def ver_status(self):
        status = [dispositivo.get_status() for dispositivo in self.dispositivos]
        return status

    def desligar_todas_luzes(self):
        list(map(lambda d: d.desligar() if isinstance(d, Luz) else None, self.dispositivos))
        self.notificar_observers("Todas as luzes foram desligadas.")

    def dispositivos_ligados(self):
        return list(filter(lambda d: d.state == 'ligada', self.dispositivos))

    def total_dispositivos_ligados(self):
        return reduce(lambda total, d: total + (1 if d.state == 'ligada' else 0), self.dispositivos, 0)

    def setar_aquecendo_todos_termostatos(self):
        list(map(lambda d: d.aquecer() if isinstance(d, Termostato) else None, self.dispositivos))
        self.notificar_observers("Todos os termostatos estão aquecendo.")

    def setar_esfriando_todos_termostatos(self):
        list(map(lambda d: d.esfriar() if isinstance(d, Termostato) else None, self.dispositivos))
        self.notificar_observers("Todos os termostatos estão esfriando.")

    def armar_todos_sistemas_seguranca(self, com_gente_em_casa=True):
        list(map(lambda d: d.armar_com_gente_em_casa() if com_gente_em_casa and isinstance(d, SistemaSeguranca) else d.armar_sem_gente_em_casa() if isinstance(d, SistemaSeguranca) else None, self.dispositivos))
        self.notificar_observers("Todos os sistemas de segurança foram armados.")

    def desarmar_todos_sistemas_seguranca(self):
        list(map(lambda d: d.desarmar() if isinstance(d, SistemaSeguranca) else None, self.dispositivos))
        self.notificar_observers("Todos os sistemas de segurança foram desarmados.")