class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        //basic T= nlogn S = o(1) 
        // sort(nums.begin(),nums.end());
        // int n = nums.size();
        // for(int i=0;i<n-1;i++)
        // {
        //     if(nums[i]==nums[i+1])
        //         return true;
        // }
        // return false;

        //better T=n S=n
        // unordered_map<int,int> um;
        // for(int i=0;i<nums.size();i++)
        //     um[nums[i]]++;
        // for(auto i:um)
        // {
        //     if(i.second>1)
        //         return true;
        // }
        // return false;

        //best T=n S=n
        // unordered_set<int> s;
        
        // for (int i = 0; i < nums.size(); i++) {
        //     if (s.find(nums[i]) != s.end()) {
        //         return true;
        //     }
        //     s.insert(nums[i]);
        // }
        // return false;
        unordered_set<int> s;
        int n = nums.size();
        for(int i=0;i<n;i++)
            s.insert(nums[i]);
        
        if(s.size()!=nums.size())
            return true;
        return false;
    }
};