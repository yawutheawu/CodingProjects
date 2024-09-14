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

int main() {
    Car car1 = Car(120,600,1200);
    std::cout << std::to_string(car1.Value) + "\n";
    std::cout << std::to_string(car1.Value2) + "\n";    
    car1.GetSecret();
    //std::cout << std::to_string(car1.SecretValue);
    std::cout << pow(2,4);
    return 0;
}