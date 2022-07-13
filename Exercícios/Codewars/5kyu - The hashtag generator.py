# https://www.codewars.com/kata/52449b062fb80683ec000024

from string import capwords as cap
def generate_hashtag(s):
    s = cap(s).replace(" ", "")
    if len(s) == 0 or len(s) > 140:
        return False
    return f"#{s}"
