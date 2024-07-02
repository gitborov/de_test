from get_json_data import get_data


url = 'https://randomuser.me/api/'
user_id = 666
data = get_data(url)[0]['contact_details']
print(get_data(url)[0]['contact_details'])
print(data)
print(user_id)
print(data.insert(0, (user_id)))
print(data)
print(5)
print([5] + data)