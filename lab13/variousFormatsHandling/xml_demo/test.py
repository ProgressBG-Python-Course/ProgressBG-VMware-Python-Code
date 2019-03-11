import xml.etree.ElementTree as ET

tree = ET.parse('prices.xml')
root = tree.getroot()


# TASK print out each:
# "product_name" - "price"


# print items attributes
print('\nAll attributes:')
for elem in root:
    # print(elem.text)
    print(elem.attrib.get('key'))

