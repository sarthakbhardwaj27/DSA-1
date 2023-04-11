brute:

sort o(nlogn)

better: o(n)

count sort, count the number of zerores one and two and print them in sequence

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero_count=0;
        int one_count=0;
        int two_count=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==0)
                zero_count++;
            else if(nums[i]==1)
                one_count++;
            else
                two_count++;
        }
        for(int i=0;i<zero_count;i++)
            nums[i]=0;
        for(int i=zero_count+0;i<zero_count+one_count;i++)
            nums[i]=1;
        for(int i=zero_count+one_count+0;i<zero_count+one_count+two_count;i++)
            nums[i]=2;
    }
};
```

best::

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low=0,mid=0,high=nums.size()-1;
        while(mid<=high){
            if(nums[mid]==0){
                swap(nums[low++],nums[mid++]);
            }
            else if(nums[mid]==1){
                mid++;
            }
            else{
                swap(nums[mid],nums[high--]);
            }
        }
    }
};