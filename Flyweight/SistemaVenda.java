package Flyweight;
// É o Cliente e Utiliza o Flyweight sem saber que ele é compartilhado
// Na verdade o papel dele é Solicitar objetos à fábrica e fornecer o estado extrínseco.

public class SistemaVenda {

    public static void main(String[] args) {

        String evento = "Show Internacional";
        String local = "Arena Central";
        String data = "10/10/2026";

        String[] cores = {"Ouro", "Prata", "Bronze"};

        // Simulação da venda de 100 mil ingressos
        for (int i = 1; i <= 100000; i++) {

            String cor = cores[i % 3];

            // Solicita o Flyweight à fábrica
            IngressoFlyweight ingresso =
                IngressoFactory.getIngresso(evento, local, data, cor);

            // Passa o estado extrínseco
            ingresso.imprimir("ID-" + i);
        }

        // Impressão
        System.out.println(
            "\nTotal de objetos criados em memória: " +
            IngressoFactory.getTotalObjetosCriados()
        );
    }
}
