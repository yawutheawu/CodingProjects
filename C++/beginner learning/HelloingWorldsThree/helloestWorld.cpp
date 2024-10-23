#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    this_thread::sleep_for(chrono::seconds(3));
    int a = 5;
    int b = a;
    a = 12;
    int c = 5;
    int* d = &c;
    c = 15;
    cout << "\n";
    cout << a << " " << b << "\n";
    cout << c << " " << *d;
    cout << "\n" << "done";
    cout << endl;
}