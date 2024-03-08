#Convert one data to another datatype is called typecasting.
# it is two type.(1)implicity---If the conversion will be automatically done is called implicity type conversion.

a=100
b=3
c=a/b
print(c)
print(type(c)) #integer to float(implicity type conversion)

a=50
b=60.3
c=a+b
print(type(c))#(implicity conversion)

#(2)Explicity type conversion---If the  the programmer will be convert one data type to anothe is callled explicity data type .
#float to int--

a=int(55.57)
print(a)
#complex to int--other to  int possible expect complex
#a=int(23+78j)
print(a)

#bool to int--
a=int(False)
print(a)

#string to int not possible..
#if string is number it convert
a=int("100")
print(a)

#other to float  conversion
a=float(10)
print(a) #int to float

#bool to float
a=float(True)
print(a)

#complex to float
#a=float(20+30j)
#print(a) #it is not possible


#string to float
a=float("2345")
print(a)

#other to complex
a=complex(10)
print(a) #int to complex

#float to complex
a=complex(12.7)
print(a)

#bool to complex
a=complex(True)
print(a)

#strng to complex
a=complex("234567")
print(a)

#other to bool
a=bool(2)
print(a)#int to bool
#complex to bool
a=bool(12+45j)
print(a)
#float to bool
a=bool(12.7)
print(a)

#string to bool
a=bool("23")
print(a)
a=bool("")
print(a)


#other to string
a=str(1)
print(a)#int to str

#complex to string
a=str(12+23j)
print(a)
#bool to str
a=str(True)
print(a)

#float to str
a=str(23.7)
print(a)