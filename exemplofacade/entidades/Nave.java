package exemplofacade.entidades;

public class Nave {
    private String nome;
    private Astronauta astronauta;

    public Nave(String _nome, Astronauta _astronauta) {
        this.nome = _nome;
        this.astronauta = _astronauta;
    }
        
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public String partir(CorpoCeleste _destino) {
        return " e partiu do(a) " + this.astronauta.getLocalAtual().gerarDescricao() +
                " para o(a) " + _destino.gerarDescricao();
    }
}
