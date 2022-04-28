import java.util.concurrent.ThreadLocalRandom;

public class Veiculos {
    private int preco;
    private String tipo;
    private int id;

    public String getTipo() {
        return tipo;
    }

    public Veiculos(int preco, String tipo) {
        this.preco = preco;
        this.tipo = tipo;
        getID();
    }

    public void getID(){
        this.id = ThreadLocalRandom.current().nextInt(10000, 100000);
    }

    public void testar(){
        System.out.println("\nID do veículo: " + id + "\nPreço por hora: " + preco + "\nTipo: " + tipo);
    }

}
