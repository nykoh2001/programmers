#include <string>
#include <vector>

#include <cmath>

using namespace std;

// 1:16 ~ 1:40

int find(int node, vector<int> &parents)
{
  if (parents[node] == node)
    return node;

  return find(parents[node], parents);
}

bool _union(int node1, int node2, vector<int> &parents)
{
  int root1 = find(node1, parents);
  int root2 = find(node2, parents);
  if (root1 == root2)
    return false;

  parents[root2] = root1;
  return true;
}

int solution(int n, vector<vector<int>> wires)
{
  int wiresSize = wires.size();
  int minDiff = pow(10, 6);
  for (int removeIdx = 0; removeIdx < wiresSize; removeIdx++)
  {
    vector<int> parents;
    for (int i = 0; i <= n; i++)
      parents.push_back(i);

    for (int idx = 0; idx < wiresSize; idx++)
    {
      if (idx == removeIdx)
        continue;

      _union(wires[idx][0], wires[idx][1], parents);
    }

    int pivotRoot = find(1, parents);
    int networkSize = 0;
    for (int i = 1; i <= n; i++)
      if (find(i, parents) == pivotRoot)
        networkSize++;

    minDiff = min(minDiff, abs(n - 2 * networkSize));
  }
  return minDiff;
}