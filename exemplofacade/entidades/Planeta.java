package exemplofacade.entidades;

public class Planeta extends CorpoCeleste {
    public Planeta(String _nome) {
        super(_nome);
        this.setTipo("Planeta");
    }
}
