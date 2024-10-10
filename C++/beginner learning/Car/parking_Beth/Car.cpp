#include <string>
#include "Car.h"
using namespace std;

Car::Car(string m, string f, int w, int s) {
    fuel = f;
    wheels = w;
    seats = s;
    model = m;
}

string Car::description() {
    return fuel + "-powered " + model;
}

