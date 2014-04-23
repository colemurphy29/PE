package problem21;

import java.util.ArrayList;
import java.util.List;
import problem21.Number;

public class Main {


	//returns in about a second, brute force though
	static List<Number> allnums1 = new ArrayList<Number>();
	static List<Number> allnums2 = new ArrayList<Number>();
	static List<Number> amicable = new ArrayList<Number>();
	
	public static void main (String [] args){
		for (int x = 1; x<10000;x++ ){
			Number num = new Number();
			List<Integer> divisorslist = new ArrayList<Integer>();
			num.setActualnum(x);
			for (int y = 1; y < x; y++){
				if (x%y == 0){
					divisorslist.add(y);
				}
			}
			int acc = 0;
			for (int b: divisorslist){
				acc = b + acc; 
			}
			num.setSummeddivisors(acc);
			allnums1.add(num); 
			allnums2.add(num);
		}
		checkdivisors();
	}
	
	static void checkdivisors(){
		for (Number n: allnums1){
			for (Number f: allnums2){
				if((n.actualnum == f.summeddivisors) && 
						(n.summeddivisors == f.actualnum) && (n.actualnum != n.summeddivisors)){
					amicable.add(n);
				}
			}
		}
		displayamicable();
	}
	
	static void displayamicable(){
		int accumulate = 0; 
		for (Number byas:amicable){
			accumulate = accumulate + byas.getActualnum(); 
		}
		System.out.println(amicable.size());
		System.out.println(accumulate);
	}
	
}
