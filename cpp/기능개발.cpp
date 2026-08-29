#include <string>
#include <vector>
#include <queue>

using namespace std;

// 큐에서 맨 앞 기능의 배포까지 걸리는 일 수 계산 + result에 push
// 해당 일 수 후 배포 가능한 상태라면 pop
// ^ 반복

// 9:05 ~ 9:32 - 81.8/100

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    int MAX_PROGRESS = 100;
    vector<int> result;
    
    queue<pair<int, int>> queued_prog;
    for (int prog_idx = 0; prog_idx < progresses.size(); prog_idx++) {
        queued_prog.push({progresses[prog_idx], prog_idx});
    }
    
    while (!queued_prog.empty()) {
        int curr_prog = queued_prog.front().first;
        int curr_prog_idx = queued_prog.front().second;
        queued_prog.pop();
        int remaining_prog = MAX_PROGRESS - curr_prog;
        
        float days_until_deploy = float(remaining_prog) / speeds[curr_prog_idx];
        if (int(days_until_deploy) < days_until_deploy) {
            days_until_deploy = int(days_until_deploy) + 1;
        }
        int deploy_batch = 1;
        
        while (!queued_prog.empty()) {
            int curr_prog = queued_prog.front().first;
            int curr_prog_idx = queued_prog.front().second;
            if (curr_prog + speeds[curr_prog_idx] * days_until_deploy < MAX_PROGRESS) {
                break;
            }
            
            queued_prog.pop();
            deploy_batch++;
        }
        result.push_back(deploy_batch);
    }
    return result;
}