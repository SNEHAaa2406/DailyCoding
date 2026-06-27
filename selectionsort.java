import java.util.*;

public class selectionsort {
    public static void main(String[] args) {
        int[] n = {45, 78, 98, 5, 4};

        for (int i = 0; i < n.length - 1; i++) {
            // Assume the current element is the smallest
            int minid = i;

            // Find the index of the smallest element
            for (int j = i + 1; j < n.length; j++) {
                if (n[j] < n[minid]) {
                    minid = j;
                }
            }

            // Swap the smallest element with the current element
            int temp = n[i];
            n[i] = n[minid];
            n[minid] = temp;
        }

        // Print the sorted array
        System.out.println("Sorted Array:");
        for (int i = 0; i < n.length; i++) {
            System.out.print(n[i] + " ");
        }
    }
}