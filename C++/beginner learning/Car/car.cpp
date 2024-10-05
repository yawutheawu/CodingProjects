//For Sleep
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

class Parking {
    private:
        int FilledSpaces = 0;
        int spaces = 1;
        int EmptySpaces = 1;
        std::vector<Car> a;
    public:
        Parking(){};
        Parking(int slots) {
            FilledSpaces = 0;
            EmptySpaces = slots;
            spaces = slots;
            a.assign(EmptySpaces, Car());
        };
        void ParkCar(Car parking, int spaceSelection) {
            if (EmptySpaces > 0) {
                if (a[spaceSelection].CheckFake() == true) {
                    a[spaceSelection] = parking;
                    FilledSpaces++;
                    EmptySpaces = spaces - FilledSpaces;
                } else {
                    std::cout << "That Slot is full!\n";
                }
            } else {
                std::cout << "No Slots!\n";
            }
        }
        void unParkCar(int spaceSelection) {
            if (a[spaceSelection].CheckFake() == false) {
                a[spaceSelection] = Car();
                FilledSpaces--;
                EmptySpaces = spaces - FilledSpaces;
            } else {
                std::cout << "That Slot is Already Empty!\n";
            }
        }
        void GetValues() {
            std::cout << "Spaces Filled: " << std::to_string(FilledSpaces) << " Available Slots: " << std::to_string(EmptySpaces);
            std::cout << "\n";
            for (Car i : a) {
                std::cout << i.Make << " " << i.Model << " ";
            }
            std::cout << "\n";
        };
};

bool TakeInput(Parking whatLot) {
    return false;
}

int main() {
    Car car1 = Car("Toyota","Highlander","KL5JD56Z85K139936");
    Car car2 = Car("BMW","M3","ZL5JD56Z840059936");
    Car car3 = Car("Chevrolet","Camaro","KQ5JD56Z85K120736");
    Car car4 = Car("Bugatti","Chiron","KL5JD56Z85K139936");
    Parking lot1 = Parking(12);
    lot1.ParkCar(car1,0);
    lot1.ParkCar(car2,1);
    lot1.ParkCar(car3,2);
    lot1.ParkCar(car4,3);
    lot1.GetValues();
    lot1.unParkCar(0);
    lot1.unParkCar(1);
    lot1.unParkCar(2);
    lot1.unParkCar(3);
    std::cout << "End of program";
    bool parker = TakeInput(lot1);
    while (parker){
        parker = TakeInput(lot1);
    }
    std::this_thread::sleep_for(std::chrono::seconds(5));
    return 0;
}