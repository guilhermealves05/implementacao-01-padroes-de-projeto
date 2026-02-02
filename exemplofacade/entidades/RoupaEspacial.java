package exemplofacade.entidades;

public abstract class RoupaEspacial {
    protected String descricao;
    
    public String gerarDescricao() {
        return " vestiu a " + descricao;
    }
}
