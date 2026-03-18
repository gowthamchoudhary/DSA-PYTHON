# Check if string is palindrome (ignore non-alphanumeric, case-insensitive)
#     Input: "A man, a plan, a canal: Panama"
#     Output: True


def valid_palindrome(sen):
    left = 0
    cleaned = ''.join(c.lower() for c in sen if c.isalnum())
    right=len(cleaned)-1
    while left<right:
        if cleaned[left]!=cleaned[right]:
            return False
        left +=1
        right -=1
    return True
sen = "A man, a plan, a canl: Panama"
print(valid_palindrome(sen))





