# Importa o módulo 'os' (Operating System).
# Ele permite que o programa interaja com as pastas e arquivos do computador.
import os

# Importa o módulo 'shutil' (Shell Utilities).
# Ele contém funções de alto nível para copiar e mover arquivos.
import shutil

# Define uma constante global que armazena o nome da pasta raiz da biblioteca.
# Usar letras maiúsculas indica que este valor não deve mudar.
PASTA_DA_BIBLIOTECA = "biblioteca"


def exibir_menu_principal():
    """
    # Descrição da tarefa:
    Esta função imprime o menu principal de opções para o usuário.
    Ela não recebe parâmetros e retorna a escolha do usuário como uma string.
    """
    
    # Imprime o título do menu.
    print("\n=== Menu da Biblioteca Digital ===")
    
    # Imprime as opções disponíveis.
    print("1. Listar todos os documentos")
    print("2. Adicionar novo documento")
    print("3. Renomear um documento")
    print("4. Remover um documento")
    print("5. Sair")
    
    # Solicita que o usuário digite um número e armazena em 'escolha'.
    escolha = input("Digite o número da sua escolha: ")
    
    # Retorna o valor que o usuário digitou.
    return escolha


def listar_documentos():
    """
    # Descrição da tarefa:
    Esta função percorre todas as pastas e subpastas dentro da PASTA_DA_BIBLIOTECA
    e imprime uma lista organizada de todos os arquivos que encontrar.
    """
    
    # Informa ao usuário que a operação de listagem foi iniciada.
    print("\n--- Listando Todos os Documentos ---")
    
    # Inicia uma variável para contar se algum arquivo foi encontrado.
    arquivos_encontrados = False
    
    # 'os.walk' é um "explorador" que anda por todas as pastas.
    # Para cada pasta, ele informa o 'caminho' dela, as 'subpastas' e os 'arquivos' nela.
    for caminho, subpastas, arquivos in os.walk(PASTA_DA_BIBLIOTECA):
        
        # Verifica se a lista de 'arquivos' nesta pasta não está vazia.
        if arquivos:
            # Se encontrou arquivos, muda a variável para True.
            arquivos_encontrados = True
            
            # Imprime o caminho da pasta para organizar a visualização.
            print(f"\n[Pasta: {caminho}]")
            
            # Itera (passa um por um) sobre cada 'nome_arquivo' na lista de 'arquivos'.
            for nome_arquivo in arquivos:
                # Imprime o nome do arquivo com um recuo.
                print(f"  - {nome_arquivo}")
    
    # Após o loop, verifica se nenhum arquivo foi encontrado em toda a biblioteca.
    if not arquivos_encontrados:
        # Informa ao usuário que a biblioteca está vazia.
        print("\nNenhum documento encontrado na biblioteca.")
        
    # Imprime uma linha final para separar o conteúdo.
    print("--------------------------------------")


def adicionar_documento():
    """
    # Descrição da tarefa:
    Esta função solicita ao usuário as informações de um novo documento.
    Ela pede o caminho de origem, o tipo e o ano.
    Em seguida, cria as pastas (ex: biblioteca/PDF/2023) e move o arquivo
    para o local correto.
    """
    
    # Informa ao usuário que a operação de adição foi iniciada.
    print("\n--- Adicionar Novo Documento ---")
    
    # Solicita ao usuário o caminho completo do arquivo de origem.
    caminho_origem = input("Digite o caminho completo do arquivo (ex: C:/Users/Downloads/artigo.pdf): ")
    
    # Solicita o tipo de documento (para criar a subpasta).
    tipo_documento = input("Digite o tipo do documento (ex: PDF, ePUB, Artigo): ").upper()
    
    # Solicita o ano de publicação (para criar a sub-subpasta).
    ano_publicacao = input("Digite o ano de publicação (ex: 2023): ")

    # O 'try' inicia um bloco de código que pode causar erros.
    # Isso é necessário para que o programa não "quebre" se algo der errado.
    try:
        # Verifica se o caminho que o usuário digitou realmente existe.
        if not os.path.exists(caminho_origem):
            # Informa um erro se o arquivo não for encontrado.
            print(f"Erro: O arquivo de origem '{caminho_origem}' não foi encontrado.")
            # 'return' para a execução da função, pois não pode continuar.
            return
            
        # Verifica se o caminho de origem é um arquivo (e não uma pasta).
        if not os.path.isfile(caminho_origem):
             print(f"Erro: O caminho '{caminho_origem}' é uma pasta, não um arquivo.")
             return

        # 'os.path.basename' pega apenas o nome do arquivo do caminho completo.
        # Ex: "C:/Users/artigo.pdf" vira "artigo.pdf".
        nome_arquivo = os.path.basename(caminho_origem)
        
        # 'os.path.join' monta o caminho da pasta de destino de forma inteligente.
        # Ex: "biblioteca", "PDF", "2023" vira "biblioteca/PDF/2023".
        pasta_destino = os.path.join(PASTA_DA_BIBLIOTECA, tipo_documento, ano_publicacao)
        
        # Monta o caminho final completo para onde o arquivo será copiado.
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)

        # 'os.makedirs' cria as pastas de destino (incluindo subpastas) se elas não existirem.
        # 'exist_ok=True' evita um erro se a pasta "biblioteca/PDF/2023" já existir.
        os.makedirs(pasta_destino, exist_ok=True)
        
        # 'shutil.copy2' copia o arquivo da origem para o destino.
        # Ele também tenta copiar os metadados (como data de criação).
        shutil.copy2(caminho_origem, caminho_destino)
        
        # Informa ao usuário que a operação foi bem-sucedida.
        print(f"Sucesso: Arquivo '{nome_arquivo}' adicionado em '{pasta_destino}'.")

    # 'except' captura erros específicos que podem acontecer dentro do 'try'.
    # 'OSError' é um erro geral do sistema (ex: permissão negada, nome de pasta inválido).
    except OSError as e:
        # Informa o erro específico que ocorreu.
        print(f"Erro ao adicionar arquivo: {e}")
    # 'Exception' captura qualquer outro erro inesperado.
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def renomear_documento():
    """
    # Descrição da tarefa:
    Esta função permite ao usuário renomear um arquivo que JÁ ESTÁ na biblioteca.
    Ela pede o caminho antigo (relativo à biblioteca) e o novo nome.
    """
    
    # Informa ao usuário que a operação de renomear foi iniciada.
    print("\n--- Renomear Documento ---")
    
    # Solicita o caminho relativo do arquivo *dentro* da biblioteca.
    caminho_antigo_relativo = input("Digite o caminho do arquivo na biblioteca (ex: PDF/2023/artigo.pdf): ")
    
    # Monta o caminho completo do arquivo antigo, juntando a pasta raiz.
    caminho_antigo_completo = os.path.join(PASTA_DA_BIBLIOTECA, caminho_antigo_relativo)
    
    # Solicita o novo nome para o arquivo (incluindo a extensão, ex: artigo_final.pdf).
    novo_nome = input("Digite o novo nome para o arquivo (ex: artigo_final.pdf): ")
    
    # Inicia o bloco de tratamento de erros.
    try:
        # Verifica se o arquivo que o usuário quer renomear realmente existe.
        if not os.path.exists(caminho_antigo_completo):
            # Informa um erro se o arquivo não for encontrado.
            print(f"Erro: O arquivo '{caminho_antigo_completo}' não foi encontrado.")
            return

        # 'os.path.dirname' extrai o diretório (pasta) onde o arquivo antigo está.
        # Ex: "biblioteca/PDF/2023/artigo.pdf" vira "biblioteca/PDF/2023".
        pasta_do_arquivo = os.path.dirname(caminho_antigo_completo)
        
        # Monta o novo caminho completo, juntando a pasta com o novo nome.
        caminho_novo_completo = os.path.join(pasta_do_arquivo, novo_nome)

        # 'os.rename' efetivamente renomeia o arquivo no sistema.
        os.rename(caminho_antigo_completo, caminho_novo_completo)
        
        # Informa ao usuário que a operação foi bem-sucedida.
        print(f"Sucesso: Arquivo renomeado para '{caminho_novo_completo}'.")

    # Captura erros do sistema operacional.
    except OSError as e:
        print(f"Erro ao renomear arquivo: {e}")


def remover_documento():
    """
    # Descrição da tarefa:
    Esta função permite ao usuário remover um arquivo da biblioteca.
    Ela pede o caminho do arquivo e solicita uma confirmação de segurança.
    """
    
    # Informa ao usuário que a operação de remoção foi iniciada.
    print("\n--- Remover Documento ---")
    
    # Solicita o caminho relativo do arquivo que deve ser removido.
    caminho_relativo = input("Digite o caminho do arquivo a ser removido (ex: PDF/2023/artigo.pdf): ")
    
    # Monta o caminho completo do arquivo.
    caminho_completo = os.path.join(PASTA_DA_BIBLIOTECA, caminho_relativo)
    
    # Inicia o bloco de tratamento de erros.
    try:
        # Verifica se o arquivo realmente existe antes de tentar remover.
        if not os.path.exists(caminho_completo):
            # Informa um erro se o arquivo não for encontrado.
            print(f"Erro: O arquivo '{caminho_completo}' não foi encontrado.")
            return

        # Pede uma confirmação final ao usuário (segurança).
        # '.lower()' converte a resposta para minúscula ("S" vira "s").
        confirmacao = input(f"Tem certeza que deseja remover '{caminho_completo}'? (s/n): ").lower()
        
        # Verifica se a resposta foi 's' (sim).
        if confirmacao == 's':
            # 'os.remove' remove o arquivo do sistema.
            os.remove(caminho_completo)
            # Informa ao usuário que a operação foi bem-sucedida.
            print("Sucesso: Arquivo removido.")
        else:
            # Informa que a operação foi cancelada.
            print("Operação cancelada.")
    
    # Captura erros do sistema operacional.
    except OSError as e:
        print(f"Erro ao remover arquivo: {e}")


def main():
    """
    # Descrição da tarefa:
    Esta é a função principal que "liga" o programa.
    Ela primeiro garante que a pasta da biblioteca exista e depois
    executa o loop do menu principal, chamando as outras funções
    com base na escolha do usuário.
    """
    
    # Garante que a pasta principal da biblioteca exista.
    # 'exist_ok=True' é importante para não dar erro se a pasta já foi criada.
    os.makedirs(PASTA_DA_BIBLIOTECA, exist_ok=True)

    # Inicia um loop infinito ('while True') para manter o menu ativo.
    # O programa só vai parar quando o usuário escolher "Sair".
    while True:
        # Chama a função que exibe o menu e armazena a escolha.
        escolha_usuario = exibir_menu_principal()
        
        # Verifica a escolha do usuário e chama a função correspondente.
        if escolha_usuario == '1':
            listar_documentos()
        elif escolha_usuario == '2':
            adicionar_documento()
        elif escolha_usuario == '3':
            renomear_documento()
        elif escolha_usuario == '4':
            remover_documento()
        elif escolha_usuario == '5':
            # Informa ao usuário que o programa está encerrando.
            print("Até logo!")
            # 'break' interrompe o loop 'while True' e encerra o programa.
            break
        else:
            # Informa ao usuário que a opção digitada não é válida.
            print("Opção inválida. Por favor, tente novamente.")

# Esta linha padrão do Python verifica se o script está sendo executado diretamente.
# Se sim (como quando você digita 'python gerenciador.py'),
# ele chama a função 'main()' para iniciar o programa.
if __name__ == "__main__":
    main()