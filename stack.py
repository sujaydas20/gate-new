n=5
while True:
 x=int(input("enter number"))
 def push(s,x):
    if top == n-1:
      print("stak i full")
      return
    if top is None:
       top =0
    else:
       top=top+1
       s[top]=x   
    