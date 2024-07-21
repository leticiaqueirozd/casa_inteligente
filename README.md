# Sistema de Casa Inteligente

### Visão Geral do Projeto
O Sistema de Casa Inteligente é uma aplicação desenvolvida em Python que tem como objetivo simular o controle e gerenciamento de dispositivos em uma casa inteligente. Através do projeto os conceitos de programação orientada a objetos, padrões de projeto, máquina de estados - biblioteca transitions - e programação funcional foram integrados no desenvolvimento permitindo a fixação do que foi visto em sala de aula na Pós Graduação em Robótica e Inteligência Artificial na Universidade Federal de Pernambuco. Meu projeto possui uma interface de linha de comando (CLI), onde o usuário pode adicionar, remover, controlar os dispositivos (classificados como: luzes, termostatos e sistemas de segurança), visualizar os dispositivos adicionados e sair da aplicação quando desejar.

### Instruções para Configurar e Executar o Projeto:

1. git clone https://github.com/leticiaqueirozd/casa_inteligente.git
2. cd casa_inteligente
3. Instale as dependências: pip install transitions
<br><br>

### Descrição dos Componentes e Padrões de Design Utilizados:
1. Classes de Dispositivos:
- src/dispositivo.py: Classe abstrata base para todos os dispositivos.
- meus_dispositivos/luz.py: Representa uma luz com estados desligada e ligada. Usa a biblioteca transitions para gerenciar estados.
- meus_dispositivos/termostato.py: Representa um termostato com estados desligado, aquecendo e esfriando.
- meus_dispositivos/sistema_seguranca.py: Representa um sistema de segurança com estados desarmado, armado_com_gente_em_casa e armado_sem_ninguem_em_casa.
2. Padrões de Projeto
- Singleton: Aplicado na classe CasaInteligente para garantir que exista apenas uma instância do sistema.
- Factory: Aplicado na classe DispositivoFactory para criar instâncias de diferentes tipos de dispositivos.
- Observer: Aplicado nas classes Observer e Subject para notificar mudanças nos estados dos dispositivos.
3. Técnicas de Programação Funcional
- Compreensões de Listas: Usadas para obter o status de todos os dispositivos no sistema.
- Map: Aplicado para controlar dispositivos em uma lista.
- Filter: Usado para filtrar dispositivos com base no estado atual.
- Reduce: Utilizado para calcular o número de dispositivos em alguma ação específica (ex: luzes ligadas).

### Exemplos de Uso da CLI
O CLI foi projetado de maneira simples para o usuário, assim ele pode facilmente fornecer as ações que ele deseja realizar através de números, como um controle remoto.
<br>
Desta forma, o usuário pode seguir o fluxo abaixo para acessar todas as funcionalidades do programa:
1. Passo 1 - Adicionar Dispositivo
2. Passo 2 - Escolher o tipo de dispositivo (Luz, Termostato, Sistema de Segurança).
3. Passo 3 - Digitar o nome do dispositivo (podendo ser por exemplo: abajur, lâmpada, luminária).
4. Passo 4 - O dispositivo será adicionado ao sistema com uma mensagem exibida.
5. Passo 5 - O usuário pode adicionar quantos dispositivos desejar porém caso queira remover algum que foi adicionado, basta "Remover Dispositivo".
6. Passo 6 - Como forma de deixar específico para o programa, qual dos dispositivos devem ser removidos da lista o usuário digita o nome do dispositivo a ser removido. Vale ressaltar que, caso esqueça o nome tem como visualizar no menu principal na parte dos "Meus dispositivos".
7. Passo 7 - O dispositivo será removido do sistema com uma mensagem exibida.
8. Passo 8 - Como proposta da atividade que é gerenciar os dispositivos, selecionando no menu a opção "Controlar dispositivo" você vai realizar as funções a depender do Tipo selecionado pois os diferentes dispositivos possuem funcionalidades distintas.
9. Passo 9 - Escolha o dispositivo a ser controlado para mostrar para o sistema qual exatamente deve ser acessado na aplicação através do nome, o tipo é reconhecido automaticamente.
10. Passo 10 - Selecionar o comando apropriado (ligar, desligar, aquecer, esfriar, etc.).
11. Passo 11 - Meus Dispositivos é uma opção para saber quais foram os dispositivos adicionados e em qual estado se encontram.
    
## Demonstração
Deixo anexo o link para visualizar o sistema funcionando, clique aqui.
