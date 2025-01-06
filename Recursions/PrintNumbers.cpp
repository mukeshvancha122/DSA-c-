#include<iostream>
using namespace std;

int printNumbers(int n){
    if(n==0){
        return 1;
    }
    else{
        cout<< n<<endl;
        return printNumbers(n-1);
    }
}
int main(){

    int result=printNumbers(4);
    cout<<result<< endl;
    return 0;
}