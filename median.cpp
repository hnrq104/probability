#include <bits/stdc++.h>


int median_algorithm(std::vector<int> vec){

    int n = vec.size();
    int size_S = int(pow(n,1.5));

    std::vector<int> S(size_S);
    for(int i = 0; i < size_S; i++){
        S.at(i) = vec.at(rand()%n);
    }
    std::sort(S.begin(),S.end());

    //now we select
    int root_n = int(sqrt(n));
    int d = size_S/2 - root_n;
    int u = size_S/2 + root_n;

    std::vector<int> C;
    C.reserve(n);

    int ld = 0, lu = 0;
    for (auto number : vec){
        if (number < S.at(d)){
            ld++;
        } else if (number > S.at(u)){
            lu++;
        } else C.push_back(number);
    }
    
    if(ld > n/2 | lu > n/2) {
        std::cout << "unlucky guy!" << std::endl;
        return 0;
    }

    std::sort(C.begin(),C.end());
    return C.at(n/2 - ld);
}