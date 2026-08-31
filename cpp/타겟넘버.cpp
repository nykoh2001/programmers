#include <string>
#include <vector>

#include <queue>
#include <array>

using namespace std;

// 1:00 ~ 1:15

int solution(vector<int> numbers, int target)
{
  queue<pair<int, int>> numberQ;
  array<int, 2> multiplier = {-1, 1};

  int lastIdx = numbers.size() - 1;
  int firstNumber = numbers[0];
  for (int mult : multiplier)
  {
    numberQ.push({mult * firstNumber, 0});
  }

  int result = 0;

  while (!numberQ.empty())
  {
    pair<int, int> numberPair = numberQ.front();
    numberQ.pop();

    int numberSum = numberPair.first;
    int newNumberIdx = numberPair.second + 1;

    for (int mult : multiplier)
    {
      int newNumberSum = numberSum + mult * numbers[newNumberIdx];
      if (newNumberIdx == lastIdx && newNumberSum == target)
        result++;

      if (newNumberIdx < lastIdx)
        numberQ.push({newNumberSum, newNumberIdx});
    }
  }
  return result;
}