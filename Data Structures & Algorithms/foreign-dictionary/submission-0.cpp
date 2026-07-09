class Solution {
public:
    string foreignDictionary(vector<string>& words) {
        int n=words.size();
        unordered_map<char,set<char>> mp;
        unordered_map<char,int> indegree;
        for(auto &x:words){
            for(auto y:x)
                indegree[y]=0;
        }
        for(int i=0;i<n-1;i++){
            auto w1=words[i];
            auto w2=words[i+1];
            if(w1.size()>w2.size() and w1.find(w2)==0)
                return "";
            for(int j=0;j<min(w1.size(),w2.size());j++){
                if(w1[j]!=w2[j]){
                    if(!mp[w1[j]].count(w2[j])){
                        mp[w1[j]].insert(w2[j]);
                        indegree[w2[j]]++;
                    }
                break;
                }
                
            }
        }
        queue<char> q;
        for(auto x:indegree)
            if(x.second==0) q.push(x.first);
        string order;
        while(!q.empty()){
            auto top=q.front();
            q.pop();
            order.push_back(top);
            for(auto x:mp[top]){
                indegree[x]--;
            if(indegree[x]==0)
                q.push(x);
            }
        }
    return order.size()==indegree.size()?order:"";
    }
};
