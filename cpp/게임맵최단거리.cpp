#include <vector>
#include <array>
#include <queue>

#include <utility>
#include <tuple>
#include <set>

using namespace std;

// 5:27 ~ 5:58 - 효율성 Fail
// ~ 6:03 - visited 대신 maps 이용

array<pair<int, int>, 4> DX_DY = {make_pair(-1, 0), make_pair(1, 0),
                                  make_pair(0, 1), make_pair(0, -1)};

vector<pair<int, int>> getMoves(vector<vector<int>> &maps, int x, int y, int xLength, int yLength)
{
  vector<pair<int, int>> moves;
  for (pair<int, int> dx_dy : DX_DY)
  {
    int newX = x + dx_dy.first;
    int newY = y + dx_dy.second;

    if (newX < 0 || newX >= xLength || newY < 0 || newY >= yLength || maps[newX][newY] == 0)
      continue;

    moves.push_back({newX, newY});
  }
  return moves;
}

int solution(vector<vector<int>> maps)
{
  int xLength = maps.size();
  int yLength = maps[0].size();

  pair<int, int> endPoint = {xLength - 1, yLength - 1};
  queue<tuple<int, int, int>> cellsToVisit;

  cellsToVisit.push(make_tuple(0, 0, 1));
  maps[0][0] = 0;

  while (!cellsToVisit.empty())
  {
    tuple<int, int, int> currCell = cellsToVisit.front();
    cellsToVisit.pop();
    int x = get<0>(currCell);
    int y = get<1>(currCell);
    int distance = get<2>(currCell);

    vector<pair<int, int>> nextMoves = getMoves(maps, x, y, xLength, yLength);
    for (pair<int, int> move : nextMoves)
    {
      if (maps[move.first][move.second] == 0)
        continue;

      if (move == endPoint)
        return distance + 1;
      cellsToVisit.push(make_tuple(move.first, move.second, distance + 1));
      maps[move.first][move.second] = 0;
    }
  }
  return -1;
}