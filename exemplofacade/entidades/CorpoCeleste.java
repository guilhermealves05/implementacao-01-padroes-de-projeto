package exemplofacade.entidades;

public class CorpoCeleste {
    private String tipo = "Corpo Desconhecido";
    private String nome;

    public CorpoCeleste(String _nome) {
        this.nome = _nome;
    }

    public String getNome() {
        return nome;
    }
    
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    
    
    
    public String gerarDescricao() {
        return this.tipo + " " + this.getNome();
    }
}
