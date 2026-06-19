import java.util.*;
public class Bubble{
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int[] n = {45, 78, 98, 4};
        for(int i=0;i<n.length-1;i++){
            for(int j=0;j<n.length-1-i;j++){
                if(n[j]>n[j+1]){
                    int temp = n[j];
                    n[j] = n[j+1];
                    n[j+1] = temp;
                }
            }
            System.out.println(n[i]);
        }

    }

}