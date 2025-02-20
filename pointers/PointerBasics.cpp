#include<iostream>
using namespace std;

int main(){

    int num=5;
    int *ptr=&num;
    cout<< num<< endl;
    cout<<"Address of the num:"<< &num <<endl;
    cout<<"Value of the num using pointer: "<< *ptr <<endl;

    return 0;
}