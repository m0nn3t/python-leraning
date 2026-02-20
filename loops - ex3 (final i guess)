numbers = [558,1, 1, 1, 222, 222, 222, 237, 287, 86, 321, 580, 252, 28, 597, 436, 175, 412, 577, 303, 305, 342, 589, 444, 256, 13, 232, 117, 381, 143, 56, 18, 526, 449, 396, 529, 362, 574, 532, 590, 582, 335, 111, 482, 360, 428, 47, 481, 45, 169, 58, 179, 413, 240, 161, 257, 103, 552, 219, 137, 363, 106, 119, 530, 461, 557, 351, 12, 195, 330, 497, 375, 42, 38, 469, 212, 551, 110, 148, 54, 495, 595, 230, 392, 539, 415, 301, 118, 107, 347, 513, 534, 44, 528, 573, 146, 129, 61, 401, 190, 555, 350, 485, 563, 440, 130, 313, 319, 448, 307, 549, 159, 245, 33, 416, 26, 596, 515, 269, 312, 451, 141, 153, 541, 395, 17, 124, 24, 578, 285, 310, 290, 203, 423, 201, 23, 265, 50, 125, 343, 462, 207, 565, 455, 154, 254, 6, 246, 308, 160, 260, 138, 302, 354, 483, 187, 72, 355, 498, 178, 314, 222, 592, 393, 220, 113, 568, 538, 356, 429, 572, 510, 315, 46, 439, 466, 152, 450, 68, 281, 112, 454, 493, 318, 293, 109, 253, 280, 540, 373, 235, 166, 264, 442, 521, 452, 346, 189, 465, 188, 566, 59, 167, 304, 387, 7, 218, 502, 371, 353, 336, 158, 262, 251, 62, 317, 370, 584, 559, 390, 434, 424, 400, 545, 418, 277, 470, 213, 282, 345, 228, 576, 522, 171, 422, 374, 180, 177, 200, 389, 114, 537, 512, 147, 600, 385, 591, 575, 299, 43, 247, 437, 48, 554, 134, 122, 484, 238, 560, 261, 379, 30, 267, 447, 542, 332, 142, 162, 209, 22, 272, 494, 275, 496, 524, 503, 127, 467, 294, 365, 15, 340, 548, 309, 464, 150, 420, 276, 517, 476, 543, 561, 233, 490, 403, 57, 585, 334, 329, 21, 341, 14, 388, 31, 296, 514, 506, 531]


six = []
results1 = 0

for i in numbers:
    if 100 <= i < 1000: 

        number = i
        suma = 0
        while number > 0:
            digit = number % 10
            suma += digit
            number = number // 10

        if suma == 6:
            six.append(i)
            if i % 3 == 0:
                results1 += 1
                if i % 9 == 0:
                    results1 -= 1
print(str(results1) + "  results 1") # nubers that have 3 digits, their digits add to 6 and can be divided by 3, but not 9

numbers_sorted = sorted(numbers[:])
print(str(numbers_sorted[-2]) + "  results 2") # second biggest number


streak = 1
max_streak = 1
streak_numbers= [numbers[0]]
max_streak_numbers = [numbers[0]]

for i in range(1,len(numbers)):
    if numbers[i-1] < numbers[i]:
        streak += 1
        streak_numbers.append(numbers[i])
    else:
        if streak > max_streak:
            max_streak = streak
            max_streak_numbers = streak_numbers[:]
        streak_numbers = [numbers[i]]
        streak = 1
        

if streak > max_streak:
    max_streak = streak
    max_streak_numbers = streak_numbers[:]

print(str(max_streak) + "  results 3") # streak of numbers that are bigger than the previous one
print(str(max_streak_numbers) + "  results 3.2")


palindromes = []
for i in numbers:
    if 1 <= i < 100:
        two = i    
        digit = two % 10
        two = two // 10
        if two == digit:
            palindromes.append(i)
    elif 100 <= i < 1000:
        three = i
        digit3 = three % 10
        three = three // 100
        if three == digit3:
            palindromes.append(i)
            
print(str(palindromes) + "  results 4") # palindromes


dupes = []
for i in range(1,len(numbers_sorted)):
    if numbers_sorted[i-1] == numbers_sorted[i]:
        dupe = numbers_sorted[i]
        dupes.append(dupe)

print(str(dupes) + "  results 5")
