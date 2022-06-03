# import dbcreds
from db_helpers import *
import os

# Start execution

run_query("INSERT INTO user (username, age) VALUES (?,?)", ["Jennifer", 50])

# Update the user whose username is jackie and set the age to 35
run_query("UPDATE user SET age=? WHERE username=?",[35,"jackie"])
users = run_query("SELECT id, username, age from user WHERE id > 5")

# Delete a user whose age is 25
run_query("DELETE from post WHERE age=?",[25])

print(users)
# Get the first person, the second field of that person
print(users[0][1])
