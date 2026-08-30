emails = [
    "ali@gmail.com", "sara@yahoo.com", "ali@gmail.com", 
    "ahmed@gmail.com", "sara@yahoo.com", "zain@hotmail.com"
]

unique_ordered_emails = list(dict.fromkeys(emails))

print("Ordered Unique Emails:")
print(unique_ordered_emails)
