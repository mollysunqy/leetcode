import java.awt.geom.NoninvertibleTransformException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;

public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        //TODO: increase speed
        ArrayList<int[]> sorted = sort(intervals);
        int i = 0;
        int size = sorted.size();
        while(i<size-1){
            int[] current = sorted.get(i);
            int j = i+1;
            boolean removed = true;
            while(removed && j<size){
                int[] next = sorted.get(j);
                if(next[0] <= current[1]){
                    current[0] = Math.min(current[0],next[0]);
                    current[1] = Math.max(current[1],next[1]);
                    sorted.remove(j);
                    size--;
                }else{
                    removed = false;
                }
            }
            i++;
        }
        int[][] merged = new int[size][2];
        for(int k=0;k<size;k++) merged[k] = sorted.get(k);
        return merged;
    }

    public ArrayList<int[]> sort(int[][] intervals){
        ArrayList<int[]> sorted = new ArrayList<>();
        for(int[] inter:intervals){
            boolean inserted = false;
            for(int i=0;i<sorted.size();i++) {
                int[] next = sorted.get(i);
                if (inter[0] < next[0]) {
                    if(next[0] <= inter[1]){
                        next[0] = Math.min(inter[0],next[0]);
                        next[1] = Math.max(inter[1],next[1]);
                    }else{
                        sorted.add(i, inter);
                    }
                    inserted = true;
                    break;
                }
            }
            if (!inserted) sorted.add(inter);
        }
        return sorted;
    }
}
