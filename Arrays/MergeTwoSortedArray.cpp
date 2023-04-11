// naive

// o((m+n)log(m+n)) space is o(1)
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i=0;i<n;i++){
            nums1[m+i]=nums2[i];
        }
        sort(nums1.begin(),nums1.end());
        
    }
};

better:
o(n+m)

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // int i=0,j=0,k=0;
        // while(i<m and j<n){
        //     if(nums1[i]<nums2[j]){
        //         nums1[k]=nums1[i];
        //         i++,k++;
        //     }
        //     else{
        //         nums1[k]=nums2[j];
        //         k++,j++;
        //     }
        // }
        // if(i<m){
        //     nums1[k]=nums1[i];
        //     k++,i++;
        // }
        // else{
        //     nums1[k]=nums1[j];
        //     k++,j++;
        // }
        int i = m-1;
        int j = n-1;
        int k = m+n-1;
        while(i>=0 && j>=0){
            if(nums1[i] > nums2[j]){
                nums1[k] = nums1[i];
                i--; k--;
            }
            else{
                nums1[k] = nums2[j];
                j--; k--;
            }
        }
        while(j>=0){
            nums1[k] = nums2[j];
            j--; k--;
        }
    }
};