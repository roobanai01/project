#include <iostream>
using namespace std;

class roar
{
public :
        float a,b,c;
        int multiplication();
        int division();
        int decrement();

        int addition()
{
        cout<<"\n---Addition Program---";
        cout<< "\nEnter the Value of A:";
        cin>>a;
        cout<< "Enter the Value of B:";
        cin>>b;
        c=a+b;

        cout<<"\nThe Added Value of " <<a <<" + " <<b<< " is:"<<c<<"\n";
}
        int subtraction()
{
        cout<<"\n---Subtraction Program---";
        cout<< "\nEnter the Value of A:";
        cin>>a;
        cout<< "Enter the Value of B:";
        cin>>b;
        c=a-b;
        cout<<"\nThe Subtracted Value of " <<a <<" - " <<b<< " is:"<<c<<"\n";
}
int increment()
{
        cout<<"\n---Increment Program---";
        cout<< "\nEnter the Value is to be increment:";
        cin>>a;
        a++;
        cout<<"\nThe Incremented Value of " <<a <<" is:"<<a<<"\n";
}
int namerepeted()
{
    int a,i;
    char name[500];
    cout<<"\n---Increment Program---";
    cout<< "\nEnter the text here:";
    cin>>name;
    cout<< "\nEnter how many times you want to repeat:";
    cin>>a;
    for(i=0;i<=a;i++)
    {
        cout<<name<<"\n";
    }
}
};
int roar :: multiplication()
{
    float a, b,c;
        cout<<"\n---Multiplication Program---";
        cout<< "\nEnter the Value of A:";
        cin>>a;
        cout<< "Enter the Value of B:";
        cin>>b;
        c=a*b;
        cout<<"\nThe Multiplied Value of " <<a <<" * " <<b<< " is:"<<c<<"\n";
}

int roar :: division()
{
    float a, b, c;
        cout<<"\n---Division Program---";
        cout<< "\nEnter the Value of A:";
        cin>>a;
        cout<< "Enter the Value of B:";
        cin>>b;
        c=a/b;
        cout<<"\nThe divided Value of " <<a <<" / " <<b<< " is:"<<c<<"\n";
}
int roar :: decrement()
{
    int a;
         cout<<"\n---Decrement Program---";
        cout<< "\nEnter the Value is to be decrement:";
        cin>>a;
        a--;
        cout<<"\nThe Decremented Value of " <<a <<" is:"<<a<<"\n";
}

class rooban{
public:
    float a,b,c;
    int addition(int a, int b);
    int namerepeted(int a, int i,char name);
    void addition()
    {
      cout<<"\n---Addition Program---";
        cout<< "\nEnter the Value of A:";
        cin>>a;
        cout<< "Enter the Value of B:";
        cin>>b;
        c=a+b;

        cout<<"\nThe Added Value of " <<a <<" + " <<b<< " is:"<<c<<"\n";
    }
};
int rooban::addition(int a, int b)
{
        c=a+b;
        cout<<"\nThe Added Value of " <<a <<" + " <<b<< " is:"<<c<<"\n";
    }
int rooban::namerepeted(int a, int i,char name)
{

    for(i=0;i<=a;i++)
    {
        cout<<name<<"\n";
    }
}

int main()
{
 roar rk;
//rk.addition();
//rk.subtraction();
//rk.multiplication();
//rk.division();
//rk.increment();
//rk.decrement();
//rk.namerepeted();
rooban rn;
//rn.addition();
//rn.addition(45,15);
//rn.namerepeted(10,0,'v');
rn.agefinder();
    return 0;
}

