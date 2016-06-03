import java.util.Scanner;

public class KTTABLE {

public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int testCases = Integer.parseInt(sc.nextLine()) ;

for (int i = 0; i < testCases; i++) {
    String a = sc.nextLine();
    String b = sc.nextLine();
    String c = sc.nextLine();
    
    int n = Integer.parseInt(a);
    String[]  talloted = b.split("\\s+");
    String[]  trequired= c.split("\\s+");
    int ans = 0 ;
    
    for(int j = 0 ; j < n; j++){
    	if(j==0){
    		if(Integer.parseInt(talloted[0]) >= Integer.parseInt(trequired[0]))
    		{//System.out.println(Integer.parseInt(talloted[0]) >= Integer.parseInt(trequired[0]));
    			ans = ans+1;}
    	}
    	else{
    		if(Integer.parseInt(talloted[j]) - Integer.parseInt(talloted[j-1]) >= Integer.parseInt(trequired[j])){
    			ans = ans + 1 ;
    		}
    	}
    }
    
    
    System.out.println(ans);
     
   
}
}
	
}	

