#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
#include "car.h"

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
                if (i.Make != ""){
                    std::cout << i.Make << " " << i.Model << ", ";
                }
            }
            std::cout << "\n";
        };
};