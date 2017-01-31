# 삽입 정렬
def insertion_sort(my_list):
    for i in range (len(my_list)):
        for i in range(len(my_list)):
            if i > 0:
                while my_list[i - 1] >= my_list[i] and i > 0:
                    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
                    i = i - 1
    return my_list

haerin = [5, 4, 3, 2, 1]
print(insertion_sort(haerin))
