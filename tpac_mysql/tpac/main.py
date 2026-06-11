from data.data_manager import carregar_dados
from ui.menus import criar_usuario_menu, painel_principal_menu
from ui.utils import exibir_cabecalho

def exibir_logo():
    import random

def exibir_frase():
    frases = [
        "😊 Que bom te ver por aqui!",
        "🚀 Vamos organizar o dia juntos?",
        "📚 Um passo de cada vez.",
        "✨ Pequenos avanços também são conquistas.",
        "🎯 Vamos focar no que importa hoje.",
        "🌟 Você está indo muito bem!",
        "🤖 Estou pronto para ajudar.",
        "💡 Toda tarefa começa com um primeiro passo.",
        "📝 Vamos colocar as ideias em ordem?",
        "😄 Pronto para mais um dia produtivo?"
    ]

    print(f"\n{random.choice(frases)}\n")

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
        exibir_frase()
        
        print("""
        ╔════════════════════════════════════╗
        ║         O QUE VAMOS FAZER?         ║
        ╠════════════════════════════════════╣
        ║ 1. Continuar com meu perfil        ║
        ║ 2. Criar um novo perfil            ║
        ║ 3. Encerrar por agora              ║
        ╚════════════════════════════════════╝
        """)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            if not dados:
                input("\nNenhum perfil salvo. Crie um primeiro! (Enter)")
                continue

                print("""
                ╔═══════════════════════════════════════╗
                ║           PERFIS ENCONTRADOS          ║
                ╠═══════════════════════════════════════╣
                """)

                    for u in dados:
                    print(f"║ 👤 {u:<33}║")

        print("╚═══════════════════════════════════════╝")

        nome = input("\n✨ Qual perfil deseja acessar? ")
            
            if nome in dados:
                painel_principal_menu(dados, nome)
            else:
                input("\n🤖🔍 Opa! Não encontrei esse perfil na minha lista. Pressione ENTER para tentar novamente.")
        elif opcao == "2":
            criar_usuario_menu(dados)
        elif opcao == "3":
            print("\nAté logo 👋, não esqueça de realizar suas tarefas diárias📝!")
            break

if __name__ == "__main__":
    executar_sistema()
