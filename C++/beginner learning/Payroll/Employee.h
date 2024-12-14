#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class Employee {
    private:
        std::string FirstName;
        std::string LastName;
        std::string EmployeeID = "000000000";
        std::string Title;
        double compensation;
        bool Wagie = false;
        double unusedVacation = 0;
        double hoursWorked = 0;
        double paidSickTime = 0;
    public:
        Employee(){}
        Employee(std::string ID,std::string NombreUno, std::string NombreDos, std::string Rank, double Payment, bool Waged = false){
            FirstName = NombreUno;
            LastName = NombreDos;
            Title = Rank;
            EmployeeID = ID;
            compensation = std::round(Payment*100.0)/100.0;
            Wagie = Waged;
        }
        std::string getName() {
            return FirstName + " " + LastName;
        }
        std::string getID() {
            return EmployeeID;
        }
        bool getWaged() {
            return Wagie;
        }
        double getComp() {
            return compensation;
        }
        double getUnsedVacation() {
            return unusedVacation;
        }
        double getHours() {
            return hoursWorked;
        }
        double getPaidSickTime() {
            return paidSickTime;
        }
        void updateTimeWorked(double newHours) {
            hoursWorked = newHours;
        }
        void updateUnusedVacation(double newVacay) {
            unusedVacation = newVacay;
        }
        void updateSickLeave(double newSickLeave) {
            paidSickTime = newSickLeave;
        }

};