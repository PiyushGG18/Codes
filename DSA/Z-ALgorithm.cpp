vector<int> zBuild(string s){
    int n = s.size();
    vector<int> z(n,0);
    int left = 0, right = 0;

    for(int i=1;i<n;i++){
        if(i <= right)
            z[i] = min(right-i+1, z[i-left]);

        
    }
}