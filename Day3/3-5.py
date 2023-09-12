# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

c_name = name1 + name2

lower_c_name = c_name.lower()

t = lower_c_name.count('t')
r = lower_c_name.count('r')
u = lower_c_name.count('u')
e = lower_c_name.count('e')

true = t+r+u+e

l = lower_c_name.count('l')
o = lower_c_name.count('o')
v = lower_c_name.count('v')
e = lower_c_name.count('e')

love = l+o+v+e

love_score = str(true)+str(love)
int_score = int(love_score)

if (int_score < 10) or (int_score > 90):
    print(f"YOur love score is {int_score}, you go together like coke and mentos.")
elif (int_score >= 40 )and (int_score <= 50):
    print(f"Your score is {int_score}, you are alright together.")
else:
    print(f"Your score is {int_score}.")

