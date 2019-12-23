#!/usr/bin/env python3

def waveList(start_value):
    adden = [21, 21, 1, 21, 1, -19, 1, -19, -19, -19, -19, -19, 1, -19, 1, 21, 1, 21, 21]
    original_list = []
    new_list = []
    new_list.append(start_value)

    for x in range(0,19):
        value = new_list[x]
        plus = adden[x]
        new_list.append(value + plus)

    print(new_list)

wav_start = [80,100,120,140,160,180]

for x in range(0,len(wav_start)):
    waveList(wav_start[x])
