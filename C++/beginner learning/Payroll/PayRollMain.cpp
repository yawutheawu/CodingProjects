#include <iostream>
#include <string>
#include <vector>
#include <cmath>

#include "Employee.h"

std::string addCommas(double number) {
    std::string output = "";
    std::string rawNum = std::to_string(number);
    output += rawNum.substr(rawNum.find("."),rawNum.length());
    int countTo3 = 0;
    int NewNum = floor(number);
    while (NewNum > 0) {
        if (countTo3 < 3) {
            countTo3++;
            output = std::to_string(NewNum%10) + output;
            NewNum = floor(NewNum/10);
        } else {
            countTo3 = 1;
            output = "," + output;
            output = std::to_string(NewNum%10) + output;
            NewNum = floor(NewNum/10);
        }
    }
    return output;
}

int main() {
    vector<Employee> employedPeoples;
    Employee numba1 = Employee("CA95294342","john", "worker", "Cashier", 17.50, true);
    Employee numba2 = Employee("CA95485738","john", "unworker", "Manager",123456789.123456789, true);
    employedPeoples.push_back(numba1);
    employedPeoples.push_back(numba2);
    for (Employee employ : employedPeoples) {
        std::cout << employ.getName() << " ";
        std::cout << "$" << addCommas(employ.getComp()) << " ";

        std::cout << "\n";
    }
    return 0;
}