x=input("Please enter a string: ")
def most_frequent(string):
    reverse=x[::-1]
    d = dict()
    for key in reverse:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
print(most_frequent(x))

