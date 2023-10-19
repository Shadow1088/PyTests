#include <iostream>
#include <stdio.h>



// //
// /*
// a   
// ss
//   s
// ss
// */




//     std::cout << "yay its working\n" ;
//     printf("Yay I can print");

//     return 0;
// }




// int main(){
//   char chr;
//     printf("The number:\n");  
//     scanf("%c", &chr);
//     printf("The input: %c", chr);

//     return 0;



// } 



int main(){
  int num;
  int returnValue;
  int countOfChar;
  do{
    printf("enter an int: ");
    returnValue = scanf("%d", &num);
    printf("%d\n", returnValue);
    
    countOfChar = 0;
    while (getchar()!='\n'){
      countOfChar++;
    }
  
  if (countOfChar>1){
    printf("There are %d characters in I/O buffer\n",countOfChar);
  }else if (countOfChar<=1){
    printf("Theres %d characters in I/O buffer\n",countOfChar);
  }
  
  if (countOfChar != 0){
    printf("The num aint 0\n");
  }
  if (num == 5){
    printf("9\n");  
  }
    

  } while (num !=0 || countOfChar != 0);


  return 0;
}


