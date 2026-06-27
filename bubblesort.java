import java.util.*;
public class bubblesort{
    public static void main(String[]args){
        Scanner sc= new Scanner(System.in);
    int[] n ={45,78,98,5};
        for(int i=0;i<=n.length-1;i++){
            for(int j=0;j<n.length-i-1;j++){
            if(n[j]>n[j+1]){
                int temp= n[j];
                n[j]=n[j+1];
                n[j+1]=temp;

            }
            }
        }

        for(int i=0;i<n.length;i++){
            System.out.print("Sorted elements are : " + n[i]);
        }

    }
    }
