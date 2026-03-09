s = "abcabcbb"

def longest_string(word):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(word)):
        while word[right] in seen:
            seen.remove(word[left])
            left += 1
        
        seen.add(word[right])
        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_string(s))