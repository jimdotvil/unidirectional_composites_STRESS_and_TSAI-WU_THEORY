'''

FROM "ENGINEERING MECHANICS OF COMPOSITE MATERIALS" BOOK
BY ISAAC M. DANIEL AND ORI ISHAI.

- MATERIAL PROPERTIES FOR 2-D UNIDIRECTIONAL COMPOSITES ARE TAKEN FROM TABLE A.4 FROM THE BOOK

- STRESS IS ROTATED FROM THE XY FRAME TO THE 12 FRAME
- IF STRESS VALUES ARE IN FUNCTION OF AN UNKNOWN VARIABLE JUST INPUT THE VALUES FOR sx, sy, ts

- FOR TSAI-WU f VALUES JUST SELECT THE MATERIAL
- THE VALUES FOR a AND b ARE CALCULATED IN ORDER TO REPRESENT THE CRITERIA EQUATION IN A QUADRATIC EQUATION. 
a FOR s^2 STRESS FACTORS. b FOR s^1 STRESS FACTORS
- THE QUADRATIC EQUATION IS SOLVED FOR THE UNKNOWN VARIABLE (SAFETY FACTOR, MAX.STRESS APPLIED IN XY FRAME)

~ JORGE JIMÉNEZ~

'''


import math

print('\nSTRESS ROTATION AND TSAI-WU THEORY CALCULATOR TOOL')
print('(Unidirectional Composites, Two-Dimensional')
print('\nINPUT ANGLE OF FIBER DIRECTION (°)=')
theta=float(input())

print('\nm value=')
m=math.cos(math.radians(theta))
print(round(m,6))
print('\nn value=')
n=math.sin(math.radians(theta))
print(round(n,6))

rotmat=[m**2,n**2,2*m*n,n**2,m**2,-2*m*n,-1*m*n,m*n,(m**2)-(n**2)]

rot=[]
for i in rotmat:
    rot.append(round(i,6))
print('\nROTATION MATRIX=')
print(rot[0:3])
print(rot[3:6])
print(rot[6:9])

print('\nINPUT STRESS (sx,sy,ts) (MPa)')
print('Input sx=')
sx=float(input())
print('Input sy=')
sy=float(input())
print('Input ts=')
ts=float(input())

print('\nSTRESS ROTATION')
print('s1=')
s1=(rot[0]*sx)+(rot[1]*sy)+(rot[2]*ts)
print(s1)
print('s2=')
s2=(rot[3]*sx)+(rot[4]*sy)+(rot[5]*ts)
print(s2)
print('t6=')
t6=(rot[6]*sx)+(rot[7]*sy)+(rot[8]*ts)
print(t6)

print('\nSELECT MATERIAL')
print('\n1 = E-GLASS/EPOXY')
print('2 = S-GLASS/EPOXY')
print('3 = KEVLAR/EPOXY (Aramid 49/Epoxy)')
print('4 = CARBON/EPOXY (AS4/3501-6)')
print('5 = CARBON/EPOXY (IM6G/3501-6)')
print('6 = CARBON/EPOXY (IM7/977-3)')
print('7 = CARBON/PEEK (AS4/APC2)')
print('8 = CARBON/POLYIMIDE (Mod I/WRD9371)')
print('9 = GRAPHITE/EPOXY (GY-70/934)')
print('10 = BORON/EPOXY (B5.6/5505)')
print('\nSELECT MATERIAL INPUT=')
sele=input()

if sele=='1':
    F1T=1140
    F1C=620
    F2T=39
    F2C=128
    F6=89
if sele=='2':
    F1T=1725
    F1C=690
    F2T=49
    F2C=158
    F6=70
if sele=='3':
    F1T=1400
    F1C=335
    F2T=30
    F2C=158
    F6=49
if sele=='4':
    F1T=2280
    F1C=1725
    F2T=57
    F2C=228
    F6=76
if sele=='5':
    F1T=2240
    F1C=1680
    F2T=46
    F2C=215
    F6=73
if sele=='6':
    F1T=3250
    F1C=1590
    F2T=62
    F2C=200
    F6=75
if sele=='7':
    F1T=2060
    F1C=1100
    F2T=78
    F2C=196
    F6=157
if sele=='8':
    F1T=807
    F1C=655
    F2T=15
    F2C=71
    F6=22
if sele=='9':
    F1T=985
    F1C=690
    F2T=29
    F2C=98
    F6=49
if sele=='10':
    F1T=1380
    F1C=1600
    F2T=56
    F2C=125
    F6=62

f1=(1/F1T)-(1/F1C)
f2=(1/F2T)-(1/F2C)
f11=(1/(F1T*F1C))
f22=(1/(F2T*F2C))
f66=(1/(F6**2))
f12=0.5*((f11*f22)**0.5)

print('\nTSAI-WU f VALUES')
print('f1= ')
print(f1)
print('f2= ')
print(f2)
print('f11= ')
print(f11)
print('f22= ')
print(f22)
print('f66=')
print(f66)
print('f12=')
print(f12)

print('\na and b values for quadratic equation')
a=(f11*(s1**2))+(f22*(s2**2))+(f66*(t6**2))+(f12*2*s1*s2)
b=(f1*s1)+(f2*s2)
c=-1
print('a=')
print(a)
print('b=')
print(b)

print('\nx value (quadratic equation solving)')
d = b**2-4*a*c # discriminant
if d < 0:
    print ("\nThis equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("\nThis equation has one solutions: ", x)
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print ("\nThis equation has two solutions: ", x1, " or", x2)
print('\n')