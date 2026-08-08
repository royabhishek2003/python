#include<bits/stdc++.h>

using namespace std;

bool onlyleft(vector<bool> &visited, string &str){
    int count=0;
    for(char &ch: str){
        if(!visited[ch-'a']) count++;
    }

    if(count==1) return true;

    return false;
}
int main(){

    string str;
    cin>>str;
    int n= str.length();
    vector<int> v(26);
    vector<bool> visited(26,false);
    for(int i=0;i<n;i++){
        if(str[i]==' '){
            cout<<"Error(space is not allowed)";
            break;
        }
        v[str[i]-'a']++;
    }

    cout<<"{";
    for(int i=0;i<n;i++){
        if(onlyleft(visited,str)){
            visited[str[i]-'a']=true;
            cout<<"'"<<str[i]<<"'"<<": "<<v[str[i]-'a'];
        }
        else if(!visited[str[i]-'a']){
            visited[str[i]-'a']=true;
            cout<<"'"<<str[i]<<"'"<<": "<<v[str[i]-'a']<<", ";
        }
    }

    cout<<"}";
    return 0;
}