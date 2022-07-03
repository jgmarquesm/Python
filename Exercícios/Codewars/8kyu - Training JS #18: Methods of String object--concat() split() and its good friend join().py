# https://www.codewars.com/kata/57280481e8118511f7000ffa

split_and_merge = lambda string, sep : f"{sep}".join([letter for j in range(0, len(string)) for letter in string[j]]).replace(f"{sep} {sep}", " ")
