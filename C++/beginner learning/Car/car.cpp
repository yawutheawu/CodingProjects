#include <iostream>
#include <cmath>

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
        }
        std::string Make;
        std::string Model;
        void GetSecret(){
            std::cout << vin;
        }
        bool CheckReal() {
            return fake;
        }
};

class Parking {
    private:
        int FilledSpaces;
        int spaces;
        int EmptySpaces;
        Car a[0];
    public:
    Parking(){};
        Parking(int slots) {
            spaces = slots;
            FilledSpaces = 0;
            EmptySpaces = spaces;
            Car a = new Car[spaces];
        }
        void ParkCar(Car parking, int spaceSelection) {
            if (EmptySpaces > 0) {
                if (a[spaceSelection].CheckReal() == false) {
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
            if (a[spaceSelection].CheckReal() == true) {
                a[spaceSelection] = Car();
                FilledSpaces--;
                EmptySpaces = spaces - FilledSpaces;
            } else {
                std::cout << "That Slot is Already Empty!\n";
            }
        }
        void GetValues() {
            std::cout << std::to_string(FilledSpaces);
            std::cout << "\n";
            for (Car i : a) {
                std::cout << i.Make << " " << i.Model << "\n";
            }
        };
};

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
    return 0;
}