# list and tuples
my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3
try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a typle")


# dictionary
empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}
print(grades["Joel"])
grades["Joel"] = 100
print(grades["Joel"])


tweet = {
    "user": "joelgrus",
    "text": "data science is awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
tweet_keys = tweet.keys()
print(tweet_keys)

tweet_values = tweet.values()
print(tweet_values)

tweet_items = tweet.items()
print(tweet_items)

print("user" in tweet_keys)
print("user" in tweet)
print("joelgrus" in tweet_values)


# sets
s= set()
s.add(1)
s.add(2)
s.add(3)
x = len(s)

# control flow
if 1 > 2:
    message = "if only 1 were greater than two"
elif 1 > 3:
    message = "else stands for else if"
else:
    message = "when all else fails use else "

# while loop
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

# for loop
for x in range(10):
    print(f"{x} is less than 10")

# continue and break
for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)