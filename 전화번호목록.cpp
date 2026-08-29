#include <string>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

/*
9:35 ~ 9:46 - 100/100, 50/100 => 91.7 / 100.0
*/

bool solution(vector<string> phone_book) {
    vector<set<string>> prefix_set_list;
    
    for (string phone_number: phone_book) {
        set<string> prefix_set;
        for (int char_idx = 0; char_idx < phone_number.size(); char_idx++) {
            prefix_set.insert(phone_number.substr(0, char_idx + 1));
        }
        prefix_set_list.push_back(prefix_set);
    }
    
    for (int phone_idx = 0; phone_idx < phone_book.size(); phone_idx++) {
        string phone_number = phone_book[phone_idx];
        for (int prefix_idx = 0; prefix_idx < phone_book.size(); prefix_idx++) {
            if (prefix_idx == phone_idx) {
                 continue;
            }
            if (prefix_set_list[prefix_idx].contains(phone_number)) {
                return false;
            }
        }
    }
    return true;
}