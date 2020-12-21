# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
your_name=name1.lower()
their_name=name2.lower()
both_name_together=your_name+their_name


#Letters repeated in the word true
t_count=both_name_together.count("t")
r_count=both_name_together.count("r")
u_count=both_name_together.count("u")
e_count=both_name_together.count("e")
total_true_count=t_count+r_count+u_count+e_count

#Letters repeated in the word love
l_count=both_name_together.count("l")
o_count=both_name_together.count("o")
v_count=both_name_together.count("v")
e_count=both_name_together.count("e")
total_love_count=l_count+o_count+v_count+e_count
total_percentage=total_true_count*10+total_love_count
if total_percentage<10 or total_percentage>90:
  print(f"Your score is {total_percentage}, you go together like coke and mentos.")
elif total_percentage>40 and total_percentage<50:
  print(f"Your score is {total_percentage}, you are alright together.")
else:
 print(f"Your score is {total_percentage}.")


