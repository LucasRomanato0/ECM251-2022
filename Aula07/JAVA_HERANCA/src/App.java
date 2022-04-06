public class App {
    public static void main(String[] args) throws Exception {
        //Ninja jiraya = new Ninja("Jiraya", "Familia", new String[]
        //{"Corte Vertical", "Corte Horizontal"});
        //System.out.println("Treinamento: "+jiraya.train());
        //System.out.println(jiraya);

        AcademicStudent naruto = new AcademicStudent("Naruto", "Uzumaki", 
        new String[]{"Jutsu dos clones da sombra", "Rasegan", "Chamar Kurama"});
        System.out.println(naruto.train());
        System.out.println(naruto.play());
        System.out.println();

        Genin ninja = new Genin("Nome", "Konoha", new String[]
        {"Jutsu 1", "Jutsu 2"}, "Coletar itens");
        System.out.println(ninja.goToMission());
        System.out.println(ninja.train());
    }
}
