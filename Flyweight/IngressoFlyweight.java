package Flyweight;

//É a interface Flyweight
//Define a operação que recebe o estado extrínseco como parâmetro.

public interface IngressoFlyweight {
    void imprimir(String idComprador); // Método que utiliza o estado extrínseco (ID do comprador)
}

