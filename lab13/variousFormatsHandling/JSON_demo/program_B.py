import json


# TODO: upload the csv example

with open('prices.json', mode='r') as fh:
  content = fh.read()

#de-serialize (unpickle) an object
received_prices = json.loads( content )

print(f'apples price: {received_prices["apples"]}')