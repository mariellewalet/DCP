""" Given a string s and a list of words words, where each word is the same length, find all starting indices of
substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"],
return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter. """

def find_concat(string: str, words: list):
    # First implementation : barbaric mode
    length_string = len(string)
    total_length = len(words)*len(words[0])
    if length_string < total_length:
        return []


    indices = []
    for word in words:
        index = string.find(word)
        start = index

        while start < length_string and index >= 0:

            substring = string[index: total_length+index]

            for i in words:
                if i not in substring:
                    break
            else:
                indices.append(index)
            start = index+1
            index = string.find(word, start)

    return indices


if __name__ == '__main__':
    print(find_concat("barfoobazbitbyte", ['dog', 'cat']))
