public class Comida extends Produto{
    private final double peso;
    private final String origem;
    private final EnumAlergias alergias;
    private final EnumTiposComida tipo;
    
    public Comida(double preco, int quantidade, String descricao, String nome, double peso, String origem,
            EnumAlergias alergias, EnumTiposComida tipo) {
        super(preco, quantidade, descricao, nome);
        this.peso = peso;
        this.origem = origem;
        this.alergias = alergias;
        this.tipo = tipo;
    }

    public double getPeso() {
        return peso;
    }

    public String getOrigem() {
        return origem;
    }

    public EnumAlergias getAlergias() {
        return alergias;
    }

    public EnumTiposComida getTipo() {
        return tipo;
    }

    @Override
    public double gerarPrecoComDesconto() {
        return getPreco()*0.95;
    }
}
