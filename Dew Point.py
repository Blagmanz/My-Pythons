
T = float(raw_input('Temperature '))
R = float(raw_input('Relative humidity'))

print 'Temperature',T ,'Relative Humidity' ,R, 
print 'dewpoint', (T - ((100-R)/2.778))
