print('intergrated-elctronics:Lab 8 Digital calculator by Jean Catulle');
print("  ")
frequency=input("Please enter your desire frequency: ");

def getvalues(frequency):
  ra=0;
  c=.000001;
  rb=1.44/(2*float(frequency)*c);
  print("Base on your inputs the recommended values are: ")
  print("Ra: %s ohm" % ra);  
  print("Rb: %s ohms" % rb);  
  print("C: 1µ farad");

getvalues(frequency);
