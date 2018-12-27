def make_pizza(size, *toppings):
    print("Size: " + str(size))
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile['key'] = value
    return profile

def sum2(a,b):
    print(a*b)