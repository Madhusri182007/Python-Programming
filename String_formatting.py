name="Madhu"
sentence=("How are you {}")
final=sentence.format(name)
print(final)
name="Jana" # the name will not change to jana
print(final)

#if you want to change the name do the following two methods
janagreeting=sentence.format("Jana")
print(janagreeting)
name="HEma"
greeting=sentence.format(name)
print(greeting)

myname="Sri"
hello=(f"How are you {myname}")
print(hello)

finalname="Kamal"
kamal_greeting=("How are you {finalname}?")
final_greeting=kamal_greeting.format(finalname="Kamal")
print(final_greeting)# this method is used to assign the values such as name    in other way we can define variable=name
greetings=kamal_greeting.format(finalname=name)
print(greetings)


'''another_greeting = f'How are you, {name}?'
print(another_greeting)'''

