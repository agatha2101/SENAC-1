from data.data_manager import carregar_dados
from ui.menus import criar_usuario_menu, painel_principal_menu
from ui.utils import exibir_cabecalho

def exibir_logo():

    print("""
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║   ██╗ █████╗ ███╗   ███╗██╗ ██████╗  ██████╗     ║
    ║   ██║██╔══██╗████╗ ████║██║██╔════╝ ██╔═══██╗    ║
    ║   ██║███████║██╔████╔██║██║██║  ███╗██║   ██║    ║
    ║   ██║██╔══██║██║╚██╔╝██║██║██║   ██║██║   ██║    ║
    ║   ██║██║  ██║██║ ╚═╝ ██║██║╚██████╔╝╚██████╔╝    ║
    ║   ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝ ╚═════╝  ╚═════╝     ║
    ║                                                  ║
    ║   Seu amigo para organizar tarefas e estudos     ║
    ║                                                  ║
    ║       Desenvolvido para auxiliar pessoas         ║
    ║            com dificuldades de foco              ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    """)

def executar_sistema():
    while True:
        dados = carregar_dados()

        exibir_logo()  

        print("Olá! 👋 Eu sou o IAmigo.")
        print("Vamos organizar suas tarefas juntos.\n")
        print("1. Entrar com seu perfil")
        print("2. Criar um novo perfil")
        print("3. Encerrar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            if not dados:
                input("\nNenhum perfil salvo. Crie um primeiro! (Enter)")
                continue
            print("\nPerfis:")
            for u in dados: print(f"- {u}")
            nome = input("\nNome do perfil: ").strip()
            if nome in dados:
                painel_principal_menu(dados, nome)
            else:
                input("\nPerfil não encontrado! (Enter)")
        elif opcao == "2":
            criar_usuario_menu(dados)
        elif opcao == "3":
            print("\nAté logo, não esqueça de realizar suas tarefas diárias!")
            break

if __name__ == "__main__":
    executar_sistema()