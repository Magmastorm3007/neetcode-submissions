class Solution {
public:

    string encode(vector<string>& strs) {
        string s="";
        for(auto &x:strs){
            s+=to_string(x.size())+"#"+x;
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string> res;
        for(int i=0;i<s.size();){
            
            int j = i;
            
            while (s[j] != '#') 
                j++;
            
            int len = stoi(s.substr(i, j - i));
            
            string str = s.substr(j + 1, len);
            res.push_back(str);
            i = j + 1 + len;
            

        }
    return res;
    }
};
