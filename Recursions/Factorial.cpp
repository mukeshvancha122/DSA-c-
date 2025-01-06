#include<iostream>

using namespace std;

int factorial(int n){

    // base condition
    if(n==0){
        return 1;
    }
    // actual formula
    else{
        return n * factorial(n-1);
    }
}
int main(){

    int result=factorial(5);
    cout<<result<<endl;
    return 0;
}