# Write a program to rename a key city to a location in the following dictionary.

sample_dict = {"name": "Kelly",
               "age": 25,
               "salary": 8000,
               "city": "New York"
               }

rename = sample_dict.pop("city")
sample_dict["location"] = rename

print(sample_dict)