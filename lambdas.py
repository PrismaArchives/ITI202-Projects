names_list=['Frank Harrelson', 'Bob Sharles', 'Bob Tranklin', 'Bob Grody', 'Hank Charles', 'Bob Rarrelson', 
'Mack Slobson', 'John Jonones', 'Rob Wranklin', 'Tom Simpsonian', 'Rob Rearrelson', 'John Moodys', 
'Frank Shones', 'John Harrelson','Frank Quhorles', 'Tom Pharles', 'Frank Fwanklin', 'Frank Charleston', 
'John Arles', 'John Georanklin', 'Frank Dobsonsoson', 'Diane Johnston', 'Dob Scone', 'Michael Scarn', 
'Goldie Hawn', 'Billie Holliday', 'Woody Harrelson', 'Arthur Rubinstein', 'Thomas Edison', 'Robert Goulet']

#sorts the strings by key last_name, which is grabbed from splitting (defaults to splitting whitespace) that
names_list.sort(key=lambda last_name: last_name.split()[1])

print(names_list)

#Sorts into a user name list that sorts based of of the 5 letters of the last name and the first 2 letters of the first name.
#Since last name is the dominant criteria, that is done last so the final result is based on that.
#Inner sorted function sorts via first name, resulting list that is sorted into first names is sorted into the final username list using last names
user_name_list = sorted(sorted(names_list, key=lambda last_name: last_name.split()[0][:1]), key=lambda first_name: first_name.split()[1][:4])

print(user_name_list)