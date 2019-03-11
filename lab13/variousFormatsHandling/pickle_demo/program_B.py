import pickle

with open('prices', mode='rb') as fh:
  content = fh.read()

#de-serialize (unpickle) an object
received_prices = pickle.loads( content )

print(f'apples price: {received_prices["apples"]}')