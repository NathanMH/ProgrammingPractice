/* Your program should emit the word as a series of elements by name with proper capitalization from the table. */

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class ChemSpelling {
    public static void main(String [] args) {
        HashMap chemHash = makeHashMap();
        checkLetters(chemHash);
    }

    private static HashMap makeHashMap() {

        String csvFile = "C:/Users/natha/Documents/ProgrammingPractice/assets/chem.csv";
        BufferedReader br = null;
        String line;
        String csvSplitBy = ",";
        HashMap<String, String> hmap = new HashMap<String, String>();

        try {
            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {
                String[] chemAbr = line.split(csvSplitBy);
                hmap.put(chemAbr[1].replace("\"", "").toLowerCase(), chemAbr[2].replace("\"", ""));
            }
        } catch (FileNotFoundException e) {
            System.out.println(e.getStackTrace());
        } catch (IOException e) {
            System.out.println(e.getStackTrace());
        }
        return hmap;
    }

    private static void checkLetters(HashMap<String, String> chash) {
        String sample = "genius";
        for(int i = 0; i < sample.length();) {
            String substring;
            if(i+2 >= sample.length()) {
                substring = String.valueOf(sample.substring(i, i+2));
                System.out.println(substring);
            } else {
                substring = String.valueOf(sample.substring(i, i+1));
                System.out.println(substring);
            }
            if(chash.get(substring) != null) {
                System.out.println("Found a 2 letter match: " + chash.get(substring));
                i+=2;
            } else if(chash.get(sample.charAt(i)) != null) {
                System.out.println("Found a single letter match: " + chash.get(sample.charAt(i)));
                i++;
            } else {
                System.out.println("No matching chem.");
                break;
            }
        }
    }
}
