#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter the size of n:";
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=n;j>=0;j--){
            cout<<j;
        }
        cout<<" "<<endl;
    }
    return 0;
}