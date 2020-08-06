'''
Longest Common Prefix
given a list of string, find the longest common prefix
example: given = ["flower", "flow", "flight"]
        :returns "fl"
'''

given = ["flower", "flowz", "flight"]


def helper(prefix, idx, given):
    if idx == len(given):
        return prefix
    i =0
    tmp_cache = ''
    while i < len(prefix) and i < len(given[idx]):
        if prefix[i] == given[idx][i]:
            tmp_cache += prefix[i]
        else:
            break
        i += 1
    return helper(tmp_cache, idx+1, given)


def longest_common_prefix(given):
    if len(helper(given[0], 1, given)) > 0:
        return helper(given[0], 1, given)
    else:
        return -1


res = longest_common_prefix(given)
print(res)