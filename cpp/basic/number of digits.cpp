#include <iostream>

using namespace std;

int main() {
  int number = 324832;
  int numberOfDigit = 0;

  while (number > 0) {
    number /= 10;
    numberOfDigit++;
  }

  cout << "number of digit: " << numberOfDigit << endl;

  return 0;
}