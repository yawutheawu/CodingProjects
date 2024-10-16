//For Sleep
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
#include "parkingVectorless.h"

Car createCar() {
    std::string NewMake;
    std::string NewModel;
    std::string NewVIN;
    try
    {
        std::cout << "Input the Make, Model and VIN seperated by spaces ";
        std::cin >> NewMake >> NewModel >> NewVIN;
        return Car(NewMake, NewModel, NewVIN);
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what();
        std::cout << '\nTry Again.\n';
        return createCar();
    }
}

std::string LowerInputString(std::string daString) {
    std::string outputString = "";
    for (char ch : daString) {
        outputString += std::tolower(ch);
    }
    return outputString;
}

bool TakeInput(Parking whatLot) {
    std::cout << "Current Parking Lot: \n";
    whatLot.ListSlots();
    std::cout << "Do you want to park a car, unpark a car, or exit? (park/unpark/exit)?: ";
    std::string UserInput = "";
    std::string UserInputTemp = "";
    std::cin >> UserInput;
    std::cout << "\n";
    UserInput = LowerInputString(UserInput);
    if (UserInput == "park"){
        UserInput = "";
        if (!whatLot.isFull()) {
            Car CarToPark = createCar();
            bool inputFlag = true;
            int SlotNum = 0;
            while (inputFlag) {
                whatLot.ListSlots();
                std::cout << "Input Slot Number to park car in: ";
                std::cin >> UserInput;
                try {
                    SlotNum = std::stoi(UserInput);
                } catch(const std::exception& e) {
                    std::cerr << e.what();
                    std::cout << '\nTry Again.\n';
                }
                if (SlotNum > 0 && SlotNum <= whatLot.LastSlot()) {
                    SlotNum--;
                    inputFlag = !whatLot.ParkCar(CarToPark, SlotNum);
                } else {
                    std::cout << "Choose an Existing Slot\n";
                }
            }
        } else {
            std::cout << "Lot is Full!\n";
        }
        return true;
    } else if (UserInput == "unpark") {
        UserInput = "";
        return true;
    } else if (UserInput == "exit") {
        UserInput = "";
        return false;
    } else {
        UserInput = "";
        std::cout << "Thats not an option!\n";
        return true;
    }
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
    lot1.ListSlots();
    lot1.unParkCar(0);
    lot1.unParkCar(1);
    lot1.unParkCar(2);
    lot1.unParkCar(3);
    bool parker = TakeInput(lot1);
    while (parker){
        parker = TakeInput(lot1);
    }
    std::cout << "End of program";
    std::this_thread::sleep_for(std::chrono::seconds(5));
    return 0;
}