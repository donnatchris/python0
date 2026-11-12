ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list.append("World!")
ft_tuple = ft_tuple[:1] + ("France!",)
ft_set.discard("tutu!")
ft_set.add("Paris!")
ft_set = set(sorted(ft_set))
ft_dict["Hello"] = "42Paris!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Expected output:
# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$