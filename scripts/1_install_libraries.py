import subprocess
import sys

# Lista das bibliotecas necessárias
required_libraries = [
    'pandas', 
    'numpy', 
    'matplotlib', 
    'seaborn', 
    'scipy'
]

# Função para instalar as bibliotecas
def install_libraries():
    for library in required_libraries:
        try:
            # Tenta importar a biblioteca
            __import__(library)
            print(f"{library} já está instalado.")
        except ImportError:
            # Se não encontrar, instala
            print(f"{library} não encontrado. Instalando...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            print(f"{library} instalado com sucesso!")

# Chama a função para instalar as bibliotecas
#
# install_libraries()
#
# Explicação do Código:
#
# Lista de Bibliotecas: A lista required_libraries contém o nome das bibliotecas que queremos verificar e instalar (se necessário).
#
# Função install_libraries: Essa função tenta importar cada biblioteca da lista. Se a importação falhar (ou seja, a biblioteca não está instalada), o script chama o pip para instalá-la automaticamente.
#
# Usando subprocess e sys: O subprocess.check_call() executa o comando de instalação do pip no terminal, e o sys.executable garante que o comando será executado no mesmo ambiente Python.