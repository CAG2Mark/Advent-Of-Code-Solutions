#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector< vector<string> > bag_types; 

void set_index(string bag) {
    bag_types.push_back(vector<string>(1, bag));
}

int get_index(string bag) {
    for (int i = 0; i < bag_types.size(); ++i) {
        if (bag_types[i][0] == bag) return i;
    }
    return -1;
}

int main() {

    const int N = 594; // number of lines in file

    for (int i = 0; i < N; ++i) {
        // assume that the input is valid, so only input the starting value
        string temp[2];
        scanf("%s%s %*s %*s", &temp[0], &temp[1]);
        
    }

    return 0;
}