class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<vector<int>> ans;
        for(int i=1;i<=n;i++){
            int left=intervals[i-1][0];
            int right = intervals[i-1][1];
            if(i<n){
                while(right>=intervals[i][0])
                {
                    right=intervals[i][1];
                    i++;
                }
            }
            ans.push_back({left,right});     
        }
        return ans;
    }
};