#include <string>
#include <vector>
#include <queue>

using namespace std;

/*
Queue, Priority Queue - methods 익히기
*/

int solution(vector<int> priorities, int location) {
    queue<pair<int, int>> process_queue;
    priority_queue<int> pq;
    
    for (int i = 0; i < priorities.size(); i++) {
        process_queue.push({priorities[i], i});
        pq.push(priorities[i]);
    }
    
    int order = 0;
    
    while (!process_queue.empty()) {
        int max_priority = pq.top();
        int curr_priority = process_queue.front().first;
        int curr_location = process_queue.front().second;
        process_queue.pop();
        
        if (curr_priority < max_priority) {
            process_queue.push({curr_priority, curr_location});
            continue;
        }
        
        if (curr_location == location) {
            return order + 1;
        }
        
        order++;
        pq.pop();
    }
}