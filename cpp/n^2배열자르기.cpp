#include <string>
#include <vector>

using namespace std;

// 1:40 ~ 1:51 - 55/100, timeout
// k번째 행 - 0~k 열까지 k+1, 그 뒤부터 열 idx + 1
// 처음부터 1차원 배열로
// int -> long long

vector<int> solution(int n, long long left, long long right)
{
  vector<int> slicedArray;
  for (long long idx = left; idx <= right; idx++)
  {
    int row = int(idx / n);
    int col = idx % n;

    if (col <= row)
    {
      slicedArray.push_back(row + 1);
      continue;
    }
    slicedArray.push_back(col + 1);
  }
  return slicedArray;
}