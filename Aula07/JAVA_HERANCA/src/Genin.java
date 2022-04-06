public class Genin extends Ninja{
       public Genin(String name, String family, String[] jutsus, String mission) {
              super(name, family, jutsus);
              this.mission = mission;
       }
       
       private String mission;

       public String goToMission(){
              return String.format("%s está indo na missão %s", getName(), mission);
       }

       @Override //fica na frente do 'train' da classe pai
       public String train(){
              return String.format("%s está treinando o jutsu %s!",
              getName(), getJutsus()[0]);
       }
}
