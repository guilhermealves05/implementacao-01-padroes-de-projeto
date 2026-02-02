# Padrões de Projeto de Software - Entrega da Implementação 1

Trabalho desenvolvido para a disciplina de Padrões de Projeto de Software. A implementação cobre os três padrões solicitados (Facade, Proxy e Flyweight), demonstrando a aplicação prática de cada um.

## Autores
* **Guilherme Alves dos Santos**
* **Paulo Cosmo da Silva Clarentino**

---

## Estrutura do Projeto (Híbrido)

Para aproveitar as melhores características de cada ambiente de desenvolvimento e dividir as responsabilidades da dupla, as implementações foram separadas da seguinte forma:

### 1. Padrão Facade (Python)
* **Arquivo:** `facade.py`
* **Descrição:** Implementação da Fachada para o Sistema de Viagem Espacial. Encapsula a complexidade da criação de astronautas, naves e escolha de roupas (Factory) em uma interface simples.

### 2. Padrão Proxy (Python)
* **Arquivo:** `proxy.py`
* **Descrição:** Implementação de Proxy Virtual para carregamento de imagens sob demanda (Lazy Loading). Simula o delay de disco e evita consumo de memória desnecessário até a exibição real.

### 3. Padrão Flyweight (Java)
* **Arquivos:** `*.java` (Na pasta do projeto Java)
* **Descrição:** Sistema de Vendas de Ingressos otimizado. Utiliza o Flyweight para garantir que milhares de ingressos compartilhem as mesmas instâncias de dados intrínsecos (Cor, Evento), economizando RAM.

---

## Como Executar

### Executando os padrões em Python (Facade e Proxy):
Certifique-se de ter o Python instalado e rode no terminal:

```bash
# Para testar o Facade (Viagem Espacial)
python facade.py

# Para testar o Proxy (Imagens)
python proxy.py