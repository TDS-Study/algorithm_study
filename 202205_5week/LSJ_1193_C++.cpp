#include <iostream>

using namespace std;

int main()
{
    int x;
    
    std::cin >> x;
    
    int i = 0;
    while (x > 0){
        ++i;
        x -= i;
    }
    
    //홀, 짝수를 구분하여 분자,분모 값 바뀜
    if(i%2 == 1){
        std::cout << 1 - x << "/" << i + x;
    }
    else{
        std::cout << i + x << "/" << 1 - x;
    }

    return 0;
}
