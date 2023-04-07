import time
import pyttsx3
engine = pyttsx3.init()
welcome_message = "Hello there! Welcome to calculator bot. I'm here to help you with your calculations. Just tell me what you need to calculate and I'll do the rest. If you need any assistance or have any questions, feel free to ask. Let's get started, shall we?"
engine.say(welcome_message)
engine.runAndWait()
engine.say("Enter your first Number")
engine.runAndWait()

a = float(input("Enter your First Number: "))

engine.say("Enter your operator")
engine.runAndWait()
b = input("Enter your Operator(+, -, *, /, ^): ")

engine.say('Enter your Second Number')
engine.runAndWait()

c = float(input("Enter your Second Number: "))

if b =="+":
    x = a + c
    engine.say("The addition of " + str(a) + "and" + str(c) + "is" + str(x))
    engine.runAndWait()
    print("The Addition of",a, "and",c, 'is: ',x )
elif b == "-":
    y = a -c
    engine.say("The Subtraction of " + str(a)+ "and" +str(c) + "is"+ str(y))
    engine.runAndWait()
    print("The Subtraction of",a, "and",c, 'is: ',y )
elif b == "*":
    z = a*c
    engine.say("The Multiplication of " + str(a) + "and" + str(c) + "is" + str(z))
    engine.runAndWait()
    print("The Multiplication of",a, "and",c, 'is: ',z)
elif b == "/":
    if c== 0:
        engine.say("We can't divide by Zero")
        engine.runAndWait()
        print("We can't divide by Zero")
    else:
        u = a/c
        engine.say("The Division of " + str(a)+ "and" +str(c) + "is"+ str(u))
        engine.runAndWait()
        print("The Divison  of",a, "and",c, 'is: ',u)
elif b == "^":
    v = a**c
    engine.say(' the result of this expression is' + str(v))
    engine.runAndWait()
    print(' the result of this expression is',v )
else:
    engine.say("Invalid operator")
    print("Invalid Operator")

str1 = "THANK YOU FOR USING "
str2 = "Developed by Uttam"
print(str1.center(50))
print(str2.upper().center(50))
time.sleep(20)
   




