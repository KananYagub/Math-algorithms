#include <iostream>
#include <cmath>
using namespace std;


int ext_euc_alg (int a, int b, int *x , int *y ) // a*x + b*y = z
{

int k = log(b) / log(2);

int r[k+1],q[k+1],u[k+1],v[k+1],i;
// cout << k<<endl;

u[0] = 1;
u[1] = 0;
v[0] = 0;
v[1] = 1;
i = 0;
r[i] = a;
r[i+1] = b;

while (r[i+1] != 0){
// cout << b<< endl;
// cout << r[i+1] << " " << q[i+1] << " " << u[i+1] << " " << v[i+1] <<endl;

q [i+2] = r[i] /r[i+1];
// val_1 = r[i+1]
r [i+2] = r[i]%r[i+1];
//r [i] = val_1;

u [i+2] = u[i] - u[i+1] * q[i+2];

v [i+2] = v[i] - v[i+1] * q[i+2];


i++;
}

int gcd_a_b = r[i];
int inv_a = u[i];
int inv_b = v[i];

*x = u[i];
*y = v[i];
return r[i];


}