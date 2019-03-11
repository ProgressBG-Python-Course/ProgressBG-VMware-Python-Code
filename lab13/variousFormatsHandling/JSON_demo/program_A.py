import json

# let's serialize a simple dict
prices = { 'apples': 2.50, 'oranges': 1.90, 'bananas': 2.40 }

# serialize the data a JSON string
serialized_prices = json.dumps( prices )
print(type(serialized_prices))



with open('prices.json', mode='w') as fh:
  fh.write(serialized_prices)


