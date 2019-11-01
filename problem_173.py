""" WWrite a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur. """

def flatten(to_flatten :dict):
    flat = {}
    for key in to_flatten.keys():
        if type(to_flatten[key]) == dict:
            for nested_key, value in flatten(to_flatten[key]).items():
                new_key = str(key) + '.' +str(nested_key)
                flat[new_key] = value
        else:
            flat[key] = to_flatten[key]
    return flat


if __name__ == '__main__':
    dictionary = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

    print(flatten(dictionary))
