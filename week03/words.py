def prefix(word1, word2):
    """Return the longest common prefix of two words."""
    i = 0
    while i < len(word1) and i < len(word2):
        if word1[i] == word2[i]:
            i += 1
        else:
            break
    return word1[0:i]

def suffix(word1, word2):
    """Return the longest common suffix of two words."""
    i = 0
    # Compare characters from right to left
    while i < len(word1) and i < len(word2):
        if word1[-(i + 1)].lower() == word2[-(i + 1)].lower():
            i += 1
        else:
            break
    # Return the matching suffix slice
    if i == 0:
        return ""
    return word1[-i:]


