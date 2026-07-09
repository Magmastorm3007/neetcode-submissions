class Solution {
public:
    vector<int> parent;
    int find(int i){
        if(i==parent[i])
            return i;
        return i=find(parent[i]);
    }

    bool union_find(int a,int b){
        a=find(parent[a]);
        b=find(parent[b]);
        if(a==b)
            return true;
        parent[b]=a;
        return false; 
    }
    int countComponents(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        for(int i=0;i<n;i++)
            parent[i]=i;
        int count=n;
        for(auto x:edges){
            if(!union_find(x[0],x[1]))
               count--;
        }
        
        
    return count;
    }
};
