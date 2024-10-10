#include "Car.h"

class Parking {

    private:
        class Space {
            public:
                Car *car;
                Space() {
                    car = nullptr;
                }
                bool isOccupied() {
                    return car != nullptr;
                }
        };
        int spots;
        int doors;
        int occupants;
        Space *spaces;
        
    public:
        Parking(int s, int d) {
            spots = s;
            doors = d;
            occupants = 0;
            spaces = new Space[s];
        }

        bool park(Car &c) {
            int i = 0;
            // find first empty parking space
            while (i < spots && spaces[i].isOccupied()) { i++; }
            if (i < spots) {
                spaces[i].car = &c;
                occupants++;
                return true;
            } else
                return false; // garage is full; can't park
        }
        bool unpark(Car &c) {
            for (int i=0; i < spots; i++) {
                if (spaces[i].car == &c) {
                    spaces[i].car = nullptr;
                    occupants--;
                    return true;
                }
            }
            return false;  // that car is not in this parking area
        }
};
