import java.util.HashSet;

public class MinimumCommonValue {
    public int getCommon(int[] nums1, int[] nums2) {
        int common = -1;
        int p1 = 0;
        int p2 = 0;
        while(p1<nums1.length && p2<nums2.length){
            if(nums1[p1] ==nums2[p2]) return nums1[p1];
            else if(nums1[p1] > nums2[p2]) p2++;
            else p1++;
        }
        return common;
    }
}
