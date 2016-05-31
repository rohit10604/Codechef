
import java.util.LinkedList;
import java.util.Scanner;

public class KGOOD {
	
	
	int min = Integer.MAX_VALUE ;
	int max = Integer.MIN_VALUE;
	
public KGOOD(){
	
}
	private int minimum (int[] a){
		min = Integer.MAX_VALUE ;
		 for(int p = 0 ; p < a.length ; p++){
			   if(a[p]!=0){  
				   if(a[p] <= min){
					   min = a[p];
				   }
			   }
		   }
		 return min ;
	}
	
	private int maximum (int[] freq){
		max = Integer.MIN_VALUE;
		  for(int p = 0 ; p < freq.length ; p++){
			   if(freq[p]!=0){  
				   if(freq[p] >= max){
					   max = freq[p];
					   
				   }
			   }
		   }
		  return max;
	}
	
	
	
	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int testCases = Integer.parseInt(sc.nextLine()) ;
	
	KGOOD r = new KGOOD();
	
	
	
	for (int k = 0; k < testCases; k++) {
		int[] freq = new int[26];  
		int kvalue = 0 ;
		//int min = Integer.MAX_VALUE ;
		//int max = Integer.MIN_VALUE;
		int maxcount = 0 ;
		
	    String a = sc.nextLine();
	    int q = 0 ;
	    while (a.charAt(q)!=' ')
		{q++;
	}
	   String word =  a.substring(0,q);
	   char[] charArray = word.toCharArray();
	   int n = Integer.parseInt(a.substring(q+1));  
	   //System.out.println(word);
	 //  System.out.println(charArray.length);
	   int y = 0 ;
	   for(char i = 'a' ; i <='z';i++ ){
		   int count = 0;
		  
		   for(int j = 0 ; j< charArray.length ; j++){
			   if(i==charArray[j]){
				   count++;
				  
			   } 
			   
		   }
		   freq[y] = count;
		   y++;
		  
	   }
	   
	  
	   
	 
	   kvalue = r.maximum(freq)- r.minimum(freq);
	  
	  
	  
	 for(int p1 = 0 ; p1 < freq.length ; p1++){ 
		 if(freq[p1]==r.maximum(freq)){
			 freq[p1]--;
			 break;
		 }
	 }
	 
	 
	 
	}    
		
	
 
	
}
}