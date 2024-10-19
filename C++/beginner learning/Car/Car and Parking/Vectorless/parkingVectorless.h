#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
#include "carVecVer.h"

class Parking {
    private:
        int FilledSpaces = 0;
        int spaces;
        int EmptySpaces;
        Car *a;
    public:
        Parking(){};
        Parking(int slots) {
            FilledSpaces = 0;
            EmptySpaces = slots;
            spaces = slots;
            a = new Car[slots];
        };
        bool ParkCar(Car parking, int spaceSelection) {
            if (EmptySpaces > 0) {
                if (a[spaceSelection].CheckFake() == true) {
                    a[spaceSelection] = parking;
                    FilledSpaces++;
                    EmptySpaces = spaces - FilledSpaces;
                    return true;
                } else {
                    std::cout << "That Slot is full!\n";
                    return false;
                }
            } else {
                std::cout << "No Slots!\n";
                return false;
            }
        }
        bool unParkCar(int spaceSelection) {
            if (a[spaceSelection].CheckFake() == false) {
                a[spaceSelection] = Car();
                FilledSpaces--;
                EmptySpaces = spaces - FilledSpaces;
                return true;
            } else {
                std::cout << "That Slot is Already Empty!\n";
                return false;
            }
        }

        void ListSlots(){
            int EnterCounter = 0;
            for (int i = 0; i < spaces; i++) {
                if (a[i].Make != ""){
                    std::cout << std::to_string(i+1) << ". " << a[i].Make << " " << a[i].Model << "    ";
                    EnterCounter++;
                }
                else {
                    std::cout << std::to_string(i+1) << ". " << "Empty Slot" << "    ";
                    EnterCounter++;
                }
                if (EnterCounter >= 3) {
                    std::cout << "\n";
                    EnterCounter = 0;
                }
            }
            std::cout << "\n";
        }

        bool isFull() {
            if (EmptySpaces == 0) {
                return true;
            } else {
                return false;
            }
        };

        bool isEmpty() {
            if (FilledSpaces == 0) {
                return true;
            } else {
                return false;
            }
        };

        int LastSlot() {
            return spaces;
        }
};