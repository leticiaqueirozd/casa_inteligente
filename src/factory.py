from meus_dispositivos.luz import Luz
from meus_dispositivos.termostato import Termostato
from meus_dispositivos.sistema_seguranca import SistemaSeguranca

class DispositivoFactory:
    @staticmethod
    def criar_dispositivo(tipo, nome):
        if tipo == 'luz':
            return Luz(nome)
        elif tipo == 'termostato':
            return Termostato(nome)
        elif tipo == 'sistema_seguranca':
            return SistemaSeguranca(nome)
        else:
            raise ValueError(f"Dispositivo desconhecido - {tipo}")
