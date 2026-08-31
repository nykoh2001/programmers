#include <iostream>

using namespace std;

void strcpy(const char* src, char* dest) {
  for (int idx = 0; src[idx] != '\0'; idx++)
    dest[idx] = src[idx];
}

int main() {
  const char* originalString = "I'm the original string";
  char copiedString[50];
  
  strcpy(originalString, copiedString);

  cout << "copied string: " << copiedString << endl;

  return 0;
}