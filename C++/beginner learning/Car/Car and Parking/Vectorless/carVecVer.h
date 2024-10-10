#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>

class Car {
    private:
        std::string vin;
        bool fake = false;
    public:
        Car(){
            fake = true;
        };
        Car(std::string Val1, std::string Val2, std::string VIN) {
            Make = Val1;
            Model = Val2;
            vin = VIN;
        };
        std::string Make;
        std::string Model;
        void GetSecret(){
            std::cout << vin;
        }
        bool CheckFake() {
            return fake;
        }
        std::string GetMakeModel() {
            return Make + " " + Model;
        }
};