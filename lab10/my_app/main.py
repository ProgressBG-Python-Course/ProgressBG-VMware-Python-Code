from packageB import get_data


def greet(user_name):
    print('Hello', user_name)

user_name = get_data.get_user_name()
print('Hello',user_name)