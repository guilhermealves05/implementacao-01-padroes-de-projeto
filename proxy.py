import time

# [INTERFACE]
# Define o contrato que as classes de imagem devem seguir.
# O Proxy e a ImagemReal implementam a mesma interface.
class Imagem:
    def exibir(self):
        raise NotImplementedError

# [REAL SUBJECT - OBJETO REAL]
# Esta é a classe "pesada". Ela simula o carregamento demorado de uma imagem do disco.
# No padrão Proxy, queremos evitar criar essa classe se não for estritamente necessário.
class ImagemDisco(Imagem):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.carregar_do_disco()
    
    def carregar_do_disco(self):
        print(f"[SISTEMA] Carregando '{self.nome_arquivo}' do disco... (Operação Pesada)")
        time.sleep(2) # Simula o delay de leitura do disco (solicitado no PDF)
        print("[SISTEMA] Carregamento concluído!")
    
    def exibir(self):
        print(f"[VISUALIZADOR] Exibindo a imagem: {self.nome_arquivo}")

# [PROXY]
# Esta classe atua como um intermediário. Ela guarda o nome do arquivo,
# mas só cria o objeto pesado (ImagemDisco) quando o método exibir() é chamado.
class ImagemProxy(Imagem):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.imagem_real = None # Começa vazio para economizar memória (Lazy Loading)
    
    def exibir(self):
        # A mágica do Proxy: verifica se já carregou. Se não, carrega agora.
        if self.imagem_real is None:
            print("[PROXY] Detectada primeira chamada. Iniciando carga real...")
            self.imagem_real = ImagemDisco(self.nome_arquivo)
        
        # Repassa a chamada para o objeto real que agora existe
        self.imagem_real.exibir()



if __name__ == "__main__":
    print("=== TESTE DO PADRÃO PROXY (PYTHON) ===")
    
    print("\n1. Instanciando o Proxy (Custo zero de memória)...")
    # O cliente cria a imagem, mas nada pesado acontece ainda.
    minha_foto = ImagemProxy("ferias_praia_4k.jpg")
    
    print("\n2. Usuário clicou no botão 'Ver Foto'...")
    # Só agora o carregamento pesado acontece (vai demorar 2s)
    minha_foto.exibir()
    
    print("\n3. Usuário clicou novamente (Cache)...")
    # Agora é instantâneo, pois o Proxy já guardou a imagem real.
    minha_foto.exibir()