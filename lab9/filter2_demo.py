names = ["Ivan", "Alex", "Maria", "Angel", ""]
filtered_names = filter(lambda s: s and s[0]=="A", names)




# task: return strings with 4 symbols only
print( list(filtered_names) )

# Ivan, Alex