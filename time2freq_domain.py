import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from scipy.special import wofz
import csv
from numpy import log 
import math

pi  = 3.1415
e = 2.71828


file = open('data/test1.csv')

type(file)
csvreader = csv.reader(file)
rows = []
xval = []
yval = []
i = 0 
for row in csvreader:
    rows.append(row)
    xval.append(row[0])
    yval.append(row[1])


xfval = []
for x in xval:
    xfval.append(float(x))
    
yfval = []
for y in yval:
    yfval.append(float(y))

xfval = np.asarray(xfval)
yfval = np.asarray(yfval)


print(type(xfval[0]))
plt.plot(xfval, yfval)
plt.xlabel("Frequency in MHz") 
plt.ylabel("Power spectrum dBm")
plt.savefig('Power spectrum')


freq = []

sampling_time = xfval[3]-xfval[2];
print('%.10f' % xfval[3])
sampling_freq = 1/sampling_time;
print('%.20f' % sampling_time)
print(sampling_freq)
sampling_freq = 1.000000000001195e9
freq = fft(xfval);
P2 = abs(freq/len(freq));
P1 = P2[:round(len(freq)/2)+1];
print(type(P1));
P1_n = [i * 5 for i in P1];
P1_n[0] = P1[0];
P1_n[len(P1)-2] = P1[len(P1)-2];
P1_n.pop()
f = []
for i in range(0,round(len(freq)/2)):
    f.append(i*sampling_freq/len(freq))
f = [float(i) for i in f];    
P1_nl = [math.log10(i)*20 for i in P1_n]
print(len(P1_n))
print(len(f))
print(type(f[1]))

fn = []
pn = []
for i in range(0,round(len(f))):
    fn.append(f[i])
    pn.append(P1_nl[i])

plt.plot(fn,pn)
plt.xlabel("Frequency in MHz") 
plt.ylabel("Power spectrum dBm")
plt.savefig('Power spectrum')