#include <string>
using namespace std;

class Car {

    private:
        string model;
        string fuel;
        int wheels;
        int seats;

    public:
        Car(string m, string f, int w, int s);

    string description();
};
