import yaml

def yaml_loader(filepath):

    with open(filepath, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    return data

info = yaml_loader('parsing/order.yaml')

for item, name in info.items():

    if item == 'invoice':
        print(item, name)

    elif item == 'bill-to':
        shipping_details = [v for v in name.values()]
        for detail in shipping_details:

            if type(detail) == dict:
                print(f'The shippings details are here:\nState: {detail["state"]}\nCity: {detail["city"]}\nPostal Code: {detail["postal"]}\nStreet Address: {detail["lines"]}')

    elif item == 'product':
        
        for product in name:
            print(f'The description: {product["description"]}\nThe price: {product["price"]}')