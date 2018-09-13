# return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.

def duplicate_count(text):
    _l = {}
    for i in text.lower() :
        if text.lower().count(i) > 1:
            _l[i] = text.lower().count(i)
        else:
            pass
    return len(_l)

print (duplicate_count('ABBA'))

# def duplicate_count(s):
# return len([c for c in set(s.lower()) if s.lower().count(c)>1])