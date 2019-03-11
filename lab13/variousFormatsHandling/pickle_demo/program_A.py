import pickle

# let's serialize a simple dict
prices = { 'apples': 2.50, 'oranges': 1.90, 'bananas': 2.40 }

#convert the object to a serialized string
serialized_prices = pickle.dumps( prices )
print(type(serialized_prices))



with open('prices_pickle.dump', mode='wb') as fh:
  fh.write(serialized_prices)


