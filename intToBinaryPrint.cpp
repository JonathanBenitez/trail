#include <iostream>

void intToBinaryPrint(int as){
int temp;
using std::cout;
bool tf = false;

 for(int i = 31; i >= 0; --i){
     
    temp =((as>>(i))&1);
    if(temp ==0 &&!tf);
    else{
    tf = true;
    cout << temp;
    }
   

}
}


int main(int argc, char* argv[]){
    using std::cout;
    using std::endl;
    cout << argv[0] << endl;
    if(argc == 1){
       //cout << "no extra arguments added " << endl;
    } else if(argc >1){
            std::cout << " More arguments added" << endl;
            for(int i = 1; i < argc; ++i){
                intToBinaryPrint(atoi(argv[i]));
                cout<< endl;
            }
    }
    
    return 0;


}