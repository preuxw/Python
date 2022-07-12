def remove_vowels_in(s, out =''):
    vowels = "aeiouy"

    if len(s) != 0 :
        if s[0] in vowels :
        
            return remove_vowels_in(s[1:],out)
        else :
            out += s[0]
            return remove_vowels_in(s[1:],out)
    return out

s = "azertyuiop"
print(remove_vowels_in(s))
