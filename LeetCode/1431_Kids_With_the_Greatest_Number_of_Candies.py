# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
# they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

def kids_with_candies(candies, extraCandies):
    result = []
    max_candy = candies.copy()
    max_candy.sort()
    max_candy = max_candy[-1]

    for kid in candies:
        if kid + extraCandies >= max_candy:
            result.append(True)
        else:
            result.append(False)

    return result

# Expected: [true, false, false, false, false]
print(kids_with_candies([4, 2, 1, 1, 2], 1))
