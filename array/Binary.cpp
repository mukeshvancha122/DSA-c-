#include<iostream>
using namespace std;

int main(){
    int n,remainder;
    cout<<"Enter the number:"<<endl;
    cin>>n;
    while(n!=0){
        remainder=n/2;
        n=n%10;
    }
    cout<<remainder<<endl;
}