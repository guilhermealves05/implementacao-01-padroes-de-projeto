package exemplofacade.entidades;

public class Astronauta {
    private String nome;
    private RoupaEspacial roupa;
    private CorpoCeleste localAtual = new Planeta("Terra");
            
    public Astronauta(String _nome) {
        this.nome = _nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }
    
    public String vestir(RoupaEspacial _roupa) {
        this.roupa = _roupa;
        if (this.roupa != null)
            return "O astronauta " + this.nome + this.roupa.gerarDescricao();
        else 
            return null;
    }

    public void setLocalAtual(CorpoCeleste _localAtual) {
        this.localAtual = _localAtual;
    }

    public CorpoCeleste getLocalAtual() {
        return localAtual;
    }
    
    
}
