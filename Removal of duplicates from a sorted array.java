class Solution {
    public int removeDuplicates(int[] nums) {
        int x;
        x=nums.length;
        for(int i=0;i<x;i++){
            if(nums[i]==nums[i+1]){
                x=x-1;
                for(int j=i;j<x;j++){
                    nums[j]=nums[j+1];
                }
            }
        }
        return x;
    }
}