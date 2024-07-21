from meus_dispositivos.luz import Luz
from meus_dispositivos.sistema_seguranca import SistemaSeguranca
from meus_dispositivos.termostato import Termostato
from src.casa_inteligente import CasaInteligente
from src.factory import DispositivoFactory

def main():
    casa = CasaInteligente()

    while True:
        print("\n>>> Menu Principal <<<\n")
        print("[1] Adicionar dispositivo")
        print("[2] Remover dispositivo")
        print("[3] Controlar dispositivo")
        print("[4] Meus dispositivos")
        print("[5] Sair")

        comando_principal = input("Digite o número do comando desejado: ").strip()

        if comando_principal == '1':
            print("\nTipos de dispositivo:")
            print("[1] Luz")
            print("[2] Termostato")
            print("[3] Sistema de Segurança")

            tipo = input("Digite o número do tipo de dispositivo: ").strip()
            nome = input("Nome do dispositivo: ").strip()

            if tipo == '1':
                dispositivo = DispositivoFactory.criar_dispositivo('luz', nome)
            elif tipo == '2':
                dispositivo = DispositivoFactory.criar_dispositivo('termostato', nome)
            elif tipo == '3':
                dispositivo = DispositivoFactory.criar_dispositivo('sistema_seguranca', nome)
            else:
                print("Tipo de dispositivo inválido!")
                continue

            casa.adicionar_dispositivo(dispositivo)
            print(f"Dispositivo '{nome}' adicionado.")
        
        elif comando_principal == '2':
            if not casa.dispositivos:
                print("\nNenhum dispositivo adicionado.")
                continue

            nome = input("Nome do dispositivo a ser removido: ").strip()
            dispositivo = next((d for d in casa.dispositivos if d.nome == nome), None)
            if dispositivo:
                casa.remover_dispositivo(dispositivo)
                print(f"Dispositivo '{nome}' removido.")
            else:
                print(f"Dispositivo '{nome}' não encontrado.")
        
        elif comando_principal == '3':
            if not casa.dispositivos:
                print("\nNenhum dispositivo adicionado.")
                continue

            nome = input("Nome do dispositivo a ser controlado: ").strip()
            dispositivo = next((d for d in casa.dispositivos if d.nome == nome), None)
            if dispositivo:
                if isinstance(dispositivo, Luz):
                    print("\nComandos para Luz:")
                    print("[1] Ligar")
                    print("[2] Desligar")

                    comando = input("Digite o número do comando: ").strip()
                    if comando == '1':
                        dispositivo.ligar()
                        print(f"Luz '{nome}' ligada.")
                    elif comando == '2':
                        dispositivo.desligar()
                        print(f"Luz '{nome}' desligada.")
                    else:
                        print("Comando inválido!")
                
                elif isinstance(dispositivo, Termostato):
                    print("\nComandos para Termostato:")
                    print("[1] Aquecer")
                    print("[2] Esfriar")
                    print("[3] Desligar")

                    comando = input("Digite o número do comando: ").strip()
                    if comando == '1':
                        dispositivo.aquecer()
                        print(f"Termostato '{nome}' aquecendo.")
                    elif comando == '2':
                        dispositivo.esfriar()
                        print(f"Termostato '{nome}' esfriando.")
                    elif comando == '3':
                        dispositivo.desligar()
                        print(f"Termostato '{nome}' desligado.")
                    else:
                        print("Comando inválido!")

                elif isinstance(dispositivo, SistemaSeguranca):
                    print("\nComandos para Sistema de Segurança:")
                    print("[1] Armar com gente em casa")
                    print("[2] Armar sem ninguém em casa")
                    print("[3] Desarmar")

                    comando = input("Digite o número do comando: ").strip()
                    if comando == '1':
                        dispositivo.armar_com_gente_em_casa()
                        print(f"Sistema de segurança '{nome}' armado com gente em casa.")
                    elif comando == '2':
                        dispositivo.armar_sem_gente_em_casa()
                        print(f"Sistema de segurança '{nome}' armado sem ninguém em casa.")
                    elif comando == '3':
                        dispositivo.desarmar()
                        print(f"Sistema de segurança '{nome}' desarmado.")
                    else:
                        print("Comando inválido!")
            else:
                print(f"Dispositivo '{nome}' não encontrado.")
        
        elif comando_principal == '4':
            if not casa.dispositivos:
                print("\nNenhum dispositivo adicionado.")
            else:
                print("\nMeus dispositivos:")
                for dispositivo in casa.dispositivos:
                    print(dispositivo.get_status())

        elif comando_principal == '5':
            print("Saindo...")
            break
        
        else:
            print("Comando inválido! Tente novamente.")

if __name__ == "__main__":
    main()
