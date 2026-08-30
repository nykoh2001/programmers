#include <string>
#include <vector>
#include <queue>

using namespace std;

// 5:16 ~ 5:27

int solution(vector<int> scoville, int K)
{
  priority_queue<int, vector<int>, greater<int>> pq;
  for (int scv : scoville)
    pq.push(scv);

  int mixFrequency = 0;

  while (pq.size() > 1 && pq.top() < K)
  {
    int firstScv = pq.top();
    pq.pop();
    int secondScv = pq.top();
    pq.pop();

    mixFrequency++;
    int newScv = firstScv + 2 * secondScv;
    pq.push(newScv);
  }

  if (pq.top() < K)
    return -1;
  return mixFrequency;
}