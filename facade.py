# --- SUBSISTEMA (CLASSES COMPLEXAS) ---
# Essas são as classes que fazem o trabalho pesado.
# No padrão Facade, elas ficam escondidas atras da fachada.
# Samuel, primeiramente eu traduzi a biblioteca das classes de JAVA para PYTHON.

class CorpoCeleste:
    # Classe base para os destinos.
    def __init__(self, nome):
        self.nome = nome
        self.tipo = "Corpo Desconhecido"

    def gerar_descricao(self):
        return f"{self.tipo} {self.nome}"

class Planeta(CorpoCeleste):
    # Representa um destino do tipo Planeta.
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Planeta"

class Lua(CorpoCeleste):
    # Representa um destino do tipo Lua.
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Lua"

class RoupaEspacial:
    # Classe abstrata/base para os tipos de roupa.
    def __init__(self):
        self.descricao = "roupa padrão"
    
    def gerar_descricao(self):
        return f" vestiu a {self.descricao}"

class RoupaParaPlaneta(RoupaEspacial):
    # Implementação concreta da roupa para planetas.
    def __init__(self):
        self.descricao = "roupa de exploração para planetas"

class RoupaParaLua(RoupaEspacial):
    # Implementação concreta da roupa para luas.
    def __init__(self):
        self.descricao = "roupa de visita a luas"

class FabricaRoupa:
    # [FACTORY METHOD]
    # Essa classe encapsula a regra de negocio para escolher a roupa.
    # O Facade usa ela para não ter que saber qual roupa combina com qual destino.
    @staticmethod
    def escolher(destino):
        if isinstance(destino, Planeta):
            return RoupaParaPlaneta()
        else:
            return RoupaParaLua()

class Astronauta:
    # Parte do subsistema. Representa quem vai viajar.
    def __init__(self, nome):
        self.nome = nome
        self.roupa = None
        self.local_atual = Planeta("Terra")
    
    # Metodo que altera o estado do astronauta (vestir).
    def vestir(self, roupa):
        self.roupa = roupa
        return f"O astronauta {self.nome}{self.roupa.gerar_descricao()}"

class Nave:
    # Parte do subsistema. Responsavel pelo transporte.
    def __init__(self, nome, astronauta):
        self.nome = nome
        self.astronauta = astronauta
    
    # Metodo que realiza a ação de viajar e gera parte do relatório.
    def partir(self, destino):
        origem_desc = self.astronauta.local_atual.gerar_descricao()
        destino_desc = destino.gerar_descricao()
        return f" e partiu do(a) {origem_desc} para o(a) {destino_desc}"


# --- A FACHADA (FACADE) ---

class EstacaoControleFacade:
    # [PADRÃO FACADE]
    # Essa é a classe principal do padrão. Ela serve como uma interface simplificada
    # para que o Cliente (Main) não precise lidar com todas as classes acima.
    
    def iniciar_viagem(self, nome_astronauta, nome_destino, tipo_destino):
        # Esse metodo orquestra tudo: cria astronauta, define destino,
        # chama a fábrica de roupas e prepara a nave.
        # Simplifica várias chamadas complexas em uma só.
        
        astronauta = Astronauta(nome_astronauta)
        
        # Define o destino (Logica simples de escolha)
        if tipo_destino.lower() == "lua":
            destino = Lua(nome_destino)
        else:
            destino = Planeta(nome_destino)
            
        # Usa a Fabrica para pegar a roupa certa sem o cliente precisar saber a logica
        roupa = FabricaRoupa.escolher(destino)
        
        # Realiza as ações sequenciais
        parte1 = astronauta.vestir(roupa)
        nave = Nave("Nave do Batman", astronauta)
        
        # Monta o relatorio final exigido
        relatorio = f"{parte1}, entrou na nave de nome {nave.nome}{nave.partir(destino)}." 
        print(relatorio)





if __name__ == "__main__":
    print("=== SISTEMA DE CONTROLE DE VIAGEM ESPACIAL (PYTHON) ===")
    
    # O cliente só conhece a Facade. nao precisa dos detalhes
    estacao = EstacaoControleFacade()

    print("\n-- Missão 1 --")
    estacao.iniciar_viagem("Guilherme Alves", "Marte", "Planeta")

    print("\n-- Missão 2 --")
    estacao.iniciar_viagem("Paulo Cosmo", "Titan", "Lua")