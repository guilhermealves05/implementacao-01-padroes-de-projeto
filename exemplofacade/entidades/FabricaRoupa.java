/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package exemplofacade.entidades;

/**
 *
 * @author sasle
 */
public class FabricaRoupa {
    public static RoupaEspacial escolher(CorpoCeleste destino) {
        if (destino instanceof Planeta) {
            return new RoupaParaPlaneta();
        } else {
            return new RoupaParaLua();
        }
    }
}
