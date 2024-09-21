#include <iostream>
#include <cmath>

class Car {
    private:
        int SecretValue;
    public:
        int Value;
        int Value2 = 10;
        void GetSecret(){
            std::cout << std::to_string(SecretValue);
        }
        Car(){};
        Car(int Val1,int Val2) {
            SecretValue = Val1;
            Value = Val2;
        }
        Car(int Val1,int Val2, int Val3) {
            SecretValue = Val1;
            Value = Val2;
            Value2 = Val3;
        }
};

class Parking {
    private:
        int spaces;
        int EmptySpaces;
        int FilledSpaces;
        Car a = Car();
    public:
    Parking(){};
        Parking(int slots, int taken_Slots, Car aTemp) {
            spaces = slots;
            FilledSpaces = taken_Slots;
            EmptySpaces = spaces - FilledSpaces;
            a = aTemp;
        }
        void GetValues() {
            std::cout << std::to_string(FilledSpaces);
            std::cout << "\n";
            a.GetSecret();
        };
};

int main() {
    Car car1 = Car(120,600,1200);
    Parking lot1 = Parking(12,1, car1);
    //std::cout << std::to_string(car1.SecretValue);
    //std::cout << pow(2,4);
    lot1.GetValues();
    return 0;
}