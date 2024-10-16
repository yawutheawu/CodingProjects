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
    cout << "\n" << "done";
    cout << endl;
}