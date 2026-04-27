n = int(input())                
A = list(map(int, input().split()))  
B = list(map(int, input().split()))  

dot = sum(a * b for a, b in zip(A, B))  #zip= А-ның бірінші санын Б-ның бірінші санымен, екіншісін екіншісімен жұптайд
#(1*4)+(2*5)+(3*6)=4+10+18=32
print(dot)                              