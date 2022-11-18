#include<stdio.h>
int main (void){
    char number[4];
    int halghe = 3 ;
    char yekan = 0;
    char a1 = 0,a2 = 0,a3 = 0,a4 = 0;
    scanf("%s",number);
    printf("your encoded number is %s  \n",number);
    while (halghe > -1) {
        yekan = number[halghe] - 48 ;
        if (yekan > 7 ){
            yekan -= 7;
        }
        else {
            yekan += 3;
        }
        if (halghe == 3) {
            a2 = yekan ;
        }
        else if  (halghe == 2){
            a1 = yekan ;
        }
        else if (halghe == 1){
            a4 = yekan;
        }
        else {
            a3 = yekan;
        }
        halghe -= 1 ;
    }
    printf("and decoded on is : %d%d%d%d",a1,a2,a3,a4);
}