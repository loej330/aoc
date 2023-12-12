#include <iostream>
#include <string>

using namespace std;

int main() {
    string line, number;
    number.resize(2);
    int total = 0;
    int i;
    while(getline(cin, line)) {
        i = 0;
        while (!isdigit(line[i])) { i++; }
        number[0] = line[i];

        i = line.length() - 1;
        while (!isdigit(line[i])) { i--; }
        number[1] = line[i];

        total += stoi(number);
    }
    cout << total;
    return 0;
}