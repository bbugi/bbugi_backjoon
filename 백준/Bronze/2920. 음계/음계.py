sound = [i for i in range(1, 9)]
sorted_sound = sorted(sound, reverse=True)
sound_list = list(map(int, input().split()))

if sorted_sound == sound_list :
    print('descending')
    
elif sound == sound_list:
    print('ascending')

else:
    print('mixed')