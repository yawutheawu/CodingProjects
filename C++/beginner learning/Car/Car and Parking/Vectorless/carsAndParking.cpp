//For Sleep
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
#include "parkingVectorless.h"

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