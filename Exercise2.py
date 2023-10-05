"

def unique_value(*args):
    for arg in args:
        return sorted(set(arg))


print(unique_value('entertaining'))
