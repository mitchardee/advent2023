#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream file("input.txt");

    string line;
    int tot = 0, first = -1, last;

    while (getline(file, line)){ 
        first = -1;
        for(char c : line)
            if(c <= '9' && c >= '0'){
                if(first < 0) first = c - '0';
                last = c - '0';
            }

        tot += first * 10 + last;
    }
    cout<<tot<<endl;
    file.close();

    return 0;
}