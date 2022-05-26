public class App {
    public static void main(String[] args) throws Exception {
        Produto manga = new Literatura(29.90, 10, "Foda pa baralho", "Gantz", "JDBC", "Alguem", 10, EnumGeneroLiteratua.ENGENHARIA);
        Produto coca = new Bebida(6.0, 8, "Presente dos deuses", "Coca-Cola", 350, EnumAlergias.GLUTEN, EnumTemperaturas.FRIO, EnumTiposBebida.REFRIGERANTE);
        Produto tepokki = new Comida(24.50, 10, "Nhoque de arroz", "Tepokki", 0.5, "Coreano", EnumAlergias.GLUTEN, EnumTiposComida.APIMENTADA);

        System.out.println("Preços Regulares: ");
        System.out.println(manga.getNome() + ": R$" + manga.getPreco());
        System.out.println(coca.getNome() + ": R$" + coca.getPreco());
        System.out.println(tepokki.getNome() + ": R$" + tepokki.getPreco());
        System.out.println("------------------------||------------------------");
        System.out.println("Preços com desconto:");
        System.out.println(manga.getNome() + getPrecoComDesconto(manga));
        System.out.println(coca.getNome() + getPrecoComDesconto(coca));
        System.out.println(tepokki.getNome() + getPrecoComDesconto(tepokki));
    }

    public static String getPrecoComDesconto(IGerarDesconto produto){
        return ": R$" + produto.gerarPrecoComDesconto();
    }
}
