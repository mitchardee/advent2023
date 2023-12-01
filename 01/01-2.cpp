#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream file("input.txt");

    string line;
    int tot = 0, first = -1, last;
    string nums[9] = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

    while (getline(file, line)){ 
        first = -1;
        for(int i = 0; i < line.length(); i++){
            if(line[i] <= '9' && line[i] >= '0'){
                if(first < 0) first = line[i] - '0';
                last = line[i] - '0';
            }
            for(int j = 0; j < 9; j++)
                if(line.substr(i, nums[j].length()) == nums[j]){
                    if(first < 0) first = j+1;
                    last = j+1;
                }
        }
        tot += first * 10 + last;
    }
    cout<<tot<<endl;
    file.close();

    return 0;
}