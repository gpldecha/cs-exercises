def is_anagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def is_anagram_hash(s1 ,s2, ):
    h = dict()
    for s in s1:
        if s in h:
            h[s] += 1
        else:
            h[s] = 1
    for s in s2:
        if s in h:
            h[s] -= 1
            if h[s] < 0:
                return False
        else:
            return False
    for _, value in h.items():
        if value != 0:
            return False
    return True

def is_anagram_26(s1 ,s2, numbers):
    for i in range(len(s1)):
        numbers[ord(s1[i]) - 97] += 1
        numbers[ord(s2[i]) - 97] -= 1
    for i in range(26):
        if numbers[i] != 0:
            return False
    return True


def sherlockAndAnagrams(s):
    n = len(s)
    anagrams = []
    numbers = [0]*26
    for w in range(1, n):
        for i in range(0, n-w+1):
            for j in range(i+1, n-w+1):
                if is_anagram_26(s[i:(i+w)], s[j:(j+w)], numbers):
                    anagrams.append((s[i:(i+w)], s[j:(j+w)]) )
                else:
                    for k in range(26):
                        numbers[k] = 0
    return anagrams


if __name__ == "__main__":
    s = 'abba'
    s = 'kkkk'
    s = 'ifailuhkqq'

    anangrams = sherlockAndAnagrams(s)
    print(' number of anagram: {}'.format(len(anangrams)))
    for anagram in anangrams:
        print(anagram)
