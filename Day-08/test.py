servers = ['web-server-01', 'db-server-01', 'app-server-01']
servers.append('web-homw-04')

servers.remove('web-homw-04')
print(servers[1:3])

my_list = [1, 2, 3, 'apple', 'banana']
print(my_list)

list_length = len(my_list)  # Length of the list (5)
print(list_length)

my_tuple = (1, 2, 'apple', 'banana')
new_tuple = my_tuple + (3.14, 'cherry')
print(my_tuple)
print(new_tuple)