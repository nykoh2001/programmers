#include <string>
#include <vector>
#include <map>
#include <algorithm> // sort
#include <cmath>     // ceil

// split
#include <sstream>
#include <iostream>

using namespace std;

// 4:20 ~ 5:15

vector<string> split(const string &str, char delimeter = ' ')
{
  vector<string> splits;
  string token;
  stringstream ss(str);
  while (getline(ss, token, delimeter))
  {
    splits.push_back(token);
  }
  return splits;
}

int hh_mm_to_minutes(string hh_mm)
{
  vector<string> hh_mm_splits = split(hh_mm, ':');
  int hh = stoi(hh_mm_splits[0]);
  int mm = stoi(hh_mm_splits[1]);
  return 60 * hh + mm;
}

vector<int> solution(vector<int> fees, vector<string> records)
{
  int basic_time = fees[0];
  int basic_fee = fees[1];
  int unit_time = fees[2];
  int unit_fee = fees[3];

  int MAX_END_MINUTES = 23 * 60 + 59;

  map<string, int> car_in_time;
  map<string, int> parking_periods;
  vector<pair<string, int>> fee_vector;

  for (string record : records)
  {
    vector<string> record_splits = split(record);
    string time = record_splits[0];
    int minutes = hh_mm_to_minutes(time);
    string car = record_splits[1];
    string in_out = record_splits[2];

    if (in_out == "IN")
    {
      car_in_time[car] = minutes;
      continue;
    }

    int in_time = car_in_time[car];
    int out_time = hh_mm_to_minutes(time);
    int parking_period = out_time - in_time;

    car_in_time.erase(car);

    if (!parking_periods[car])
      parking_periods[car] = 0;
    parking_periods[car] += parking_period;
  }

  for (auto iter = car_in_time.begin(); iter != car_in_time.end(); iter++)
  {
    string car = iter->first;
    int in_time = iter->second;
    int parking_period = MAX_END_MINUTES - in_time;

    if (!parking_periods[car])
      parking_periods[car] = 0;
    parking_periods[car] += parking_period;
  }

  for (auto iter = parking_periods.begin(); iter != parking_periods.end(); iter++)
  {
    string car = iter->first;
    int parking_period = iter->second;
    if (parking_period <= basic_time)
    {
      fee_vector.push_back({car, basic_fee});
      continue;
    }
    int fee = basic_fee;
    int exceed_time = parking_period - basic_time;
    fee += ceil(float(exceed_time) / unit_time) * unit_fee;
    fee_vector.push_back({car, fee});
  }

  sort(fee_vector.begin(), fee_vector.end());
  vector<int> fee_result;

  for (pair<string, int> fee : fee_vector)
  {
    fee_result.push_back(fee.second);
  }
  return fee_result;
}