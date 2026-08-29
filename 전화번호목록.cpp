#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
9:35 ~ 9:46 - 100/100, 50/100 => 91.7 / 100.0
9:52 ~ 10:05 - map (중단)
10:05 ~ 10:08 - sort
*/

bool solution(vector<string> phone_book)
{
  sort(phone_book.begin(), phone_book.end());

  for (int phone_idx = 0; phone_idx < phone_book.size() - 1; phone_idx++)
  {
    string current = phone_book[phone_idx];
    string next = phone_book[phone_idx + 1];

    if (next.size() >= current.size() && next.compare(0, current.size(), current) == 0)
    {
      return false;
    }
  }
  return true;
}