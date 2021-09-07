#include <iostream>    // Importing Libraries

using namespace std;   // Using Standard Namespace

int main() {

    //------------------------------Data Types------------------------------
    
    // 1. Integer

    int integer = 10;
    int neg_integer = -5;
    int anotherInteger = 2988;


    // 2. Float

    float this_is_a_float = 5.49;
    float negative_float = -7.802;
    float zeroFloat = 0.0;


    // 3. String

    string name = "Toha";
    string language = "C++";
    string president = "Abdul Hamid";


    // 4. Character
    
    char this_is_c = 'c';
    char this_is_also_a_character = '4';
    char this_too = ')';

    
    // 5. Boolean

    bool I_am_intelligent = false;
    bool python_is_awesome = true;
    bool thisIsFalse = 0;
    bool this_isTrue = 1;


    // 6. Signed and Unsigned

    signed int negative_or_positive = -5;    // A signed integer (NOT float) can be both positive or negative
    unsigned int onlyPositive = 5;   // Unsigned integer (NOT float) can be only positive
    /* The following statement would cause an error
                           unsigned float onlyPositiveFloat = 45.789;                      */


    // Double, Long and Short

    double this_is_a_double_floating_thingy = 76.67;         //  I don't know what these do. But it is something
    long int longInteger = 12;                               //  with the memory. A normal int would allocate 4 
    short int shortInteger = 13;                             //  bytes (32 bits) depending on the OS but a double
    double doubleInteger = 11;                               //  would allocate twice that, 8 bytes. long and short
                                                             //  are also something like this I guess...




    // Multi Dimensional Arrays

            //  These are like normal arrays but their syntax is like 
            //  int multiArr[size1][size2]...[sizeN]

    int multiArr[2][3][2] = 
    {
        {{1, 4}, {5, 7}, {12, 3}},
        {{-6, 4}, {5, -9}, {0, -11}}
    };

    


    // Pointers

                //  A pointer is a variable, with the address of another variable as its value.
                //  In C++, pointers help make certain tasks easier to perform. Other tasks, such
                //  as dynamic memory allocation, cannot be performed without using pointers.

                //  All pointers share the same data type - a long hexadecimal number that
                //  represents a memory address.

    int num = 88;
    int *numPointer = &num;     // numPointer is the pointer here.

        //  NOTE

            //  *numPointer will return value of num.
            //  If you do      
            //  cout << *numPointer;
            //  It will print 88.

            //  But if you do
            //  cout << numPointer;
            //  It will print the memory address.




    // Correct way to declare variables. (For DYNAMIC memory)

    int *number = new int;
    *number = 100;

      //  Let's suppose you have finished working with number i.e. you will not use it anymore.

    delete number;

      //  This is done to free up memory.
      //  You can reuse the pointer that is pointing to a non
      //  existing memory location/address.

    number = new int;
    *number =  109;

        //  NOTE
            
            //  To call this number variable in any calculation or anything,
            //  you must use *number instead of number. Calling number would
            //  return the memory location/address, calling *number would 
            //  return the value stored in that location/address

    

    //  Dynamic Memory for 2d matrix/array


    //# of rows and columns 
    int row=4,col=5; 
    //Dinamically allocating 2D Matrix 
    int **Mat_2D = new int*[row]; 
    for (int i=0; i<row; i++) 
    {
        Mat_2D[i] = new int[col];
    }
     
    //Assigning and printing values 
    for(int c=0; c<col; c++)
    { 
        for(int r=0; r<row; r++) 
            { 
              Mat_2D[r][c] = r * c; 
              cout << Mat_2D[r][c] << " "; 
            } 
        cout<<endl; 
    } 
    //Free the memory 
    for(int r=0; r<row; r++)
    {
        delete [] Mat_2D[r];
        delete[] Mat_2D;
        return 0; 
    
    }



    return 0;
}