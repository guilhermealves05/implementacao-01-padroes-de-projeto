package Flyweight;

//Essa é a classe concreta que implementa o Flyweight
//Aqui essa classe contém o estado intríseco ou seja, os dados compartilháveis

public class Ingresso implements IngressoFlyweight {

    // ESTADO INTRÍNSECO é o que vai ser compartilhado no PAdrão
    private String evento;
    private String local;
    private String data;
    private String cor;

    // Construtor define os dados que NÃO mudam entre os ingressos
    public Ingresso(String evento, String local, String data, String cor) {
        this.evento = evento;
        this.local = local;
        this.data = data;
        this.cor = cor;
    }

    // Método recebe o ESTADO EXTRÍNSECO
    @Override
    public void imprimir(String idComprador) { // Esse ID não é atributo da classe, ele é passado dinamicamente
        System.out.println(
            "Evento: " + evento +
            " | Local: " + local +
            " | Data: " + data +
            " | Cor: " + cor +
            " | ID Comprador: " + idComprador
        );
    }
}
