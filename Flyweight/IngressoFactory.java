package Flyweight;

//Controla a criação e a reutilização dos objetos
//Ele garante que não existam objetos duplicados em memória

import java.util.HashMap;
import java.util.Map;

public class IngressoFactory {

    // Cache de objetos Flyweight
    private static Map<String, IngressoFlyweight> cache = new HashMap<>();

    public static IngressoFlyweight getIngresso(
            String evento, String local, String data, String cor) {

        // Chave única baseada no estado intrínseco
        //A chave identifica combinações únicas de estado intrínseco
        String chave = evento + "-" + local + "-" + data + "-" + cor;

        // Cria apenas se ainda não existir
        if (!cache.containsKey(chave)) {
            cache.put(chave, new Ingresso(evento, local, data, cor));
        }

        // Retorna sempre o objeto compartilhado
        return cache.get(chave);
    }

    // Método apenas para fins de relatório (exigido no enunciado)
    public static int getTotalObjetosCriados() {
        return cache.size();
    }
}
