public class PandigitalRomanNumerals {

    public static void main(String [] args) {

        int[] hundreds = {400, 600};
        int[] tens = {40, 60};
        int[] ones = {4, 6};

        System.out.println("Pandigital Roman Numbers");
        for(int one : ones) {
            for(int ten : tens) {
                for (int hundred: hundreds) {
                    int total = 1000 + one + ten + hundred;
                    System.out.println(total);
                }
            }
        }
    }
}
