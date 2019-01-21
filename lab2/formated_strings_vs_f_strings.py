user_name = "ada"
user_age = 32


# next two statements do equivalent job
print(f"Hello {user_name.capitalize()}. After ten years you'll be {user_age+10} years old.")


print("Hello {}. After ten years you'll be {} years old.".format(user_name.capitalize(), user_age+10))