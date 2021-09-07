#include <iostream>
#include<bits/stdc++.h> 

using namespace std;

int sum(int a, int b)
{
    int sum = a + b;
    return sum;
}

void name(string a)
{
    cout << "Your name is " << a << endl;
}

string invName(string a)
{
    cout << "Inverse of " << a << " is ";
    reverse(a.begin(), a.end());
    cout << a;
    return  a;
}


int main()
{
    cout << "Assalamu Alaikum." << endl
        << "Do sum(a, b) to add a and b." << endl
        << "Do name(name) to display your name." << endl
        << "Do invName(name) to see the inverse of your name." << endl
        << endl
        << "Some examples are given..." << endl;

        sum(3, 6);
        cout << endl;

        name("Kabbo");
        
        invName("Kabbo");
        cout << endl << "Thank You";


        return 0;
}
