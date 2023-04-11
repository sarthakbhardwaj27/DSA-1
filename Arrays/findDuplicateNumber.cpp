// o(n) + space(n)

// ```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int,int> um;
        for(auto i:nums){
            if(um[i]==1)
                return i;
            um[i]++;
        }
        return -1;
    }
};


// o(n) space(1) but modifies the array

// ```cpp
class Solution {
public:
    int findDuplicate(vector<int>& a) {
        for(int i=0;i<a.size();i++)
        {
            if(a[abs(a[i])]<0)
                return abs(a[i]);
            else
                a[abs(a[i])]*=(-1);
        }  
        return -1;
    }
};


// slow and fast pointer method (linked list)

// ```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];
        do{
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        while(slow!=fast);
        fast = nums[0];
        while(slow!=fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};


// other’s solutions:
 int findDuplicate(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
       cin.tie(NULL) ;
        while(nums[0]!= nums[nums[0]])
        swap(nums[0],nums[nums[0]]);

        return nums[0];