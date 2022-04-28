public class Usuario {
    private String nome;
    private Veiculos veiculos;

    public Usuario(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Usuario: " + nome;
    }

    public void alugar(Veiculos veiculos){
        this.veiculos = veiculos;
    }
}
