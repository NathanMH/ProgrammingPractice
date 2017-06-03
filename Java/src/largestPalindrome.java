package largestPalindrome;

public class largestPalindrome {
    static int largestPalindrome = 0;

    public static boolean checkPalindrome(int sum){
        String s = Integer.toString(sum);    

        for(int i = 0, j = s.length() - 1; i < s.length()/2; i++, j--){
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args){
        long startTime = System.nanoTime();
        System.out.println("Starting @ " + startTime);
    	for(int i = 999; i > 111; i--){
            for(int j = 999; j > 111; j--){
                int product = i * j;
                if(checkPalindrome(product) && (product > largestPalindrome)){
                    largestPalindrome = product;
                }
            }
        }
        long endTime = System.nanoTime();
        System.out.println("The largest palindrome is " + largestPalindrome);
        long time = endTime - startTime;
        System.out.println("This process took " + (double)time/1000000000 + " seconds.");
    }
}
