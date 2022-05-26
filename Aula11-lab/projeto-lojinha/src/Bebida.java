public class Bebida extends Produto{
    private final int volume;
    private final EnumAlergias alergias;
    private final EnumTemperaturas temperatura;
    private final EnumTiposBebida tipo;
    
    public Bebida(double preco, int quantidade, String descricao, String nome, int volume, EnumAlergias alergias,
            EnumTemperaturas temperatura, EnumTiposBebida tipo) {
        super(preco, quantidade, descricao, nome);
        this.volume = volume;
        this.alergias = alergias;
        this.temperatura = temperatura;
        this.tipo = tipo;
    }

    public int getVolume() {
        return volume;
    }

    public EnumAlergias getAlergias() {
        return alergias;
    }

    public EnumTemperaturas getTemperatura() {
        return temperatura;
    }

    public EnumTiposBebida getTipo() {
        return tipo;
    }

    @Override
    public double gerarPrecoComDesconto() {
        return getPreco()*0.9;
    }
}
