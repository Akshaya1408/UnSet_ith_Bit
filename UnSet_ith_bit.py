def unset_bit(num,bit):
    n=(1<<bit)
    if num&n:
        num=num&~n
    return num

num=int(input())
bit=int(input())
print(unset_bit(num,bit))