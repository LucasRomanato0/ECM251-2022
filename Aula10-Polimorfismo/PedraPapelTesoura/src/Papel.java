public class Papel extends Jogada{

       public Papel() {
           super(EnumJogadas.PEDRA, EnumJogadas.SPOKE);
       }
   
       @Override
       public EnumJogadas getTipo() {
           return EnumJogadas.PAPEL;
       }

    @Override
    public String toString() {
        return String.join("\n",
        "                                                ",
        "                                                ",
        "                                                ",
        "                 ...........                    ",
        "              ....          ...                 ",
        "            ..                 ...              ",
        "          ..                      ..            ",
        "        ..                          .           ",
        "       .                             ..         ",
        "      .                        .      ..        ",
        "     .                       :: .. --:  .       ",
        "    .                       -.   :-. ..  .      ",
        ":  .                      .=    .+.  :-  ..     ",
        "-:.                      .:    ::    :.   .     ",
        ".:.                     -.    ::    .-     .    ",
        " .                     =     ::     -..     .   ",
        ".                    .-     .:    .-  -.    .   ",
        ".                :: .:     ::    .-   :.     .  ",
        ".              .-:..=.     :.     -   .:      .  ",
        ".            ==.   -.     :.     =    :          ",
        ".          .=    .:.     :.     -    :.        . ",
        ".          :    ::     .:.     :    :+:        . ",
        ".         ..  .:.     .:      :    .+.-:       . ",
        ".        .-  .-       .      -.    +. ..        .",
        ".       .- .-.             .-     -:  ::        .",
        ".      .: .:              .-     :.   :         .",
        ".      . -.               .     :.   :.         .",
        ".     ..=                      :.    -          .",
        ".     :.                      :.   .-           .",
        ".     :                      ..   .-            .",
        ".    .-                      -    :.            .",
        ".    ..                     =    :.             .",
        ".    -                          .:             . ",
        ".    :                         ::              . ",
        ".   -                         ::               . ",
        ".   *                         :                . ",
        ".  .=                        ::               .  ",
        "..::.                       .:                .  ",
        ".:.                        .:                 .  ",
        ".                         ::                 .   ",
        ".                        ::                 ..   ",
        ".                       ::                  .    ",
        " ..                  .:.                  .     ",
        ".::.                 .-                   .      ",
        ".:.                 .-                   ..      ",
        " ");
    }
       
   }