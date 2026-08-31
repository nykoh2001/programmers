#include <iostream>

using namespace std;

void swap(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

int main() {
  int a = 20;
  int b = 14;

  cout << "Before:" << endl;
  cout << "a: " << a << ", b: " << b << endl;

  swap(a, b);

  cout << "After:" << endl;
  cout << "a: " << a << ", b: " << b << endl;

  return 0;
}