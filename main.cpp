
#include <iostream>
#include<cstring>
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
class kumar{
public:

void condition()
{int a;
int i;
cout<<"Enter the value:";
cin>>a;
switch(a)
{
case 1:
    for(i=0;i<=10;i++)
    {
        cout<<"Rooban is a good boy.\n";
    }
        break;

 case 2:
    for(i=0;i<=10;i++)
    {

        cout<<"Vinu is a good boy.\n";
    }
        break;

case 3:
    for(i=0;i<=10;i++)
    {

        cout<<"Kalai is a good boy.\n";
    }
        break;
}
}
void condition1()
{
    int l=0;
    char a[500];
    cout<<"Enter the string:";
    cin.getline(a,500);
    l=strlen(a);
    cout<<"The length of the string("<<a<<") is:"<<l;
}
void condition2()
{
    int b;
    int c;
    char a[500];
    cout<<"Enter the value:";
    cin>>b;
    cout<<"select Square or Cube:";
    cin>>a;
    if(strcmp(a,"square")==0)
    {
c=b*b;
cout<<"The Square value of the "<<b<<"is:"<<c;
    }
    else if(strcmp(a,"cube")==0)
    {
c=b*b*b;
cout<<"The Cube value of the "<<b<<"is:"<<c;
    }
else
{
    cout<<"You entered the wrong option";
}
}
};


int main()
{
 roar rk;
//rk.addition();
//rk.subtraction();
//rk.multiplication();
//rk.division();
//rk.increment();
//rk.decrement();

rooban rn;
//rn.addition();
//rn.addition(45,15);

kumar kr;
//kr.condition();
//kr.condition1();
kr.condition2();
    return 0;
}

