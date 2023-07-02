#include <iostream>
using namespace std;

int delivery(int n)
{
    int sample1=5, sample2=3, sam1=1, sam2=1;


    while(n>=sample1*sam1)
    {
        if(n==sample1*sam1)
            return sam1;
        sam1++;
    }

    sam1=1;
    while(n>sample1*(sam1+1)) sam1++;
    while(sam1>=0)
    {
        sam2=1;
        while(n>=sample1*sam1+ sample2*sam2)
        {
            if(n==sample1*sam1+ sample2*sam2)
                return (sam1+sam2);
            sam2++;
        }
        sam1--;
    }
    return -1;
}
int main(){
    int n;
    cin>>n;
    cout<<delivery(n)<<endl;
    return 0;
}
