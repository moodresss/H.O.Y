pi=float(3.1415926535)
print('этапы работы программы:\n1)расчёт объёма маховика \n2)расчёт массы маховика\n3)расчёт момента инерции \n4)расчёт угловой скорости \n5)расчёт энергии')

#1
print(' \nэтап_1')
r1=float(input('наружный радиус маховика'))
r2=float(input('внутренний радиус маховика'))
z=float(input('ширина маховика'))
v = float(((r1**2)-(r2**2))*pi*z)
print('объём=',v)

#2
print(' \nэтап_2')
p=float(input('плотность материала маховика='))
m=p*v
print('масса=',m,'кг')

#3
print(' \nэтап_3')
I=float(0.5*m*(r1**2+r2**2))
print('момент инерции массы=',I)

#4
print(' \nэтап_4')
f=float(input('частота вращения(ГЦ)='))
w=float(2*pi*f)
print('угловая скорость=',w)

#5
print(' \nэтап_5')
e=float(0.5*I*w**2)
print('кинетическая энергия=',e)
sssr=(input('любой символ с клавиатуры для выхода'))
