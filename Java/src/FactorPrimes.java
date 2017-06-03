package primeFactors;

import java.util.*;

public class FactorPrimes{
    public static void main(String[] args){
        long number = 600851475143L;
        int divisor = 3;
        List<Integer> primes = new ArrayList<Integer>();

        for(; number > 1; divisor += 2){
            while(number % divisor == 0){
                number /= divisor;
                primes.add(divisor);
            }
        } 
        for(int i : primes){
            System.out.print(i + " ");
        }
        System.out.println(divisor-2);
    }
}
