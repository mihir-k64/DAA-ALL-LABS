#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <limits>

struct Employee {
    std::string employeeID;
    int basicSalary;
    int hra;
    int da;
    int conveyanceAllowance;
    int otherAllowances;
    int pf;
    int professionalTax;
    int incomeTax;
    int grossSalary;
    int netSalary;
};

int main() {
    // Change the file path if necessary
    std::ifstream file("employee_salaries.csv"); 
    std::string line, word;
    std::vector<Employee> employees;

    // Skip the header line
    std::getline(file, line);

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        Employee emp;

        std::getline(ss, emp.employeeID, ',');
        ss >> emp.basicSalary; ss.ignore();
        ss >> emp.hra; ss.ignore();
        ss >> emp.da; ss.ignore();
        ss >> emp.conveyanceAllowance; ss.ignore();
        ss >> emp.otherAllowances; ss.ignore();
        ss >> emp.pf; ss.ignore();
        ss >> emp.professionalTax; ss.ignore();
        ss >> emp.incomeTax; ss.ignore();

        // Calculate Gross Salary
        emp.grossSalary = emp.basicSalary + emp.hra + emp.da + emp.conveyanceAllowance + emp.otherAllowances;

        // Calculate Net Salary
        emp.netSalary = emp.grossSalary - (emp.pf + emp.professionalTax + emp.incomeTax);

        employees.push_back(emp);
    }

    int maxNetSalary = std::numeric_limits<int>::min();
    int minNetSalary = std::numeric_limits<int>::max();
    std::string maxSalaryEmployee, minSalaryEmployee;

    for (const auto& emp : employees) {
        if (emp.netSalary > maxNetSalary) {
            maxNetSalary = emp.netSalary;
            maxSalaryEmployee = emp.employeeID;
        }
        if (emp.netSalary < minNetSalary) {
            minNetSalary = emp.netSalary;
            minSalaryEmployee = emp.employeeID;
        }
    }

    std::cout << "Employee with Maximum Net Salary: " << maxSalaryEmployee << " with " << maxNetSalary << "\n";
    std::cout << "Employee with Minimum Net Salary: " << minSalaryEmployee << " with " << minNetSalary << "\n";

    return 0;
}
