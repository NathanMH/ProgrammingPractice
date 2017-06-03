package sieveOfEratosthenes;

import java.util.ArrayList;

public class PrimeTester {
	public static void main(String[] args){
		ArrayList<Integer> primes = Sieve.findPrimes(20);
		
		for(int i : primes){
			System.out.println(i);
		}
	}
}
