for word in [x for x in iter(input, 'end')]:
    f_w = word[:len(word) // 2]
    s_w = word[len(f_w) + 1:] if len(word) & 1 else word[len(f_w):]

    while f_w:
        if f_w != s_w:
            f_w = f_w[:- 1]
            s_w = s_w[1:]
        else:
            br = word[:len(word) - len(f_w)]
            br = br[len(f_w):]
            if br:
                print(br + f_w + br)
            break

'''
input:
aba
asdthisasd
baumyaubau
end

output:
bab
thisasdthis
myaubaumyau
'''
