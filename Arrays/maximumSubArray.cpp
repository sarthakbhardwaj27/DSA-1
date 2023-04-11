class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // int ans = INT_MIN;
        // int n=nums.size();
        // int sum=0;
        // for(int i=0;i<n;i++){
        //     sum = max(nums[i],sum+nums[i]);
        //     if(sum>ans)
        //         ans=sum;
        // }
        // return ans;
        int sum=0;
        int maxsum=INT_MIN;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            sum+=nums[i];
            if(maxsum<sum)
                maxsum=sum;
            if(sum<0)
                sum=0;
        }
        return maxsum;
    }
};

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = INT_MIN;
        int n=nums.size();
        for(int gap=0;gap<n;gap++){
            int temp_sum=0;
            for(int j=0;j<n;j++){
                if((j+gap)<n){
                    temp_sum+=nums[j+gap];
                    ans=max(ans,temp_sum);
                }
            }
        }
        return ans;
    }
};