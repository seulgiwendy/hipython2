# 두 리스트 합치기
def merge(list1, list2):
    new_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    new_list += list1[i:]
    new_list += list2[j:]

    return new_list

# 합병 정렬
def merge_sort(my_list):
    # Base Case
    if len(my_list) < 2:
        return my_list

    # Recursive Case: left와 right로 my_list를 나누어준다.
    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    # Recursive Case: my_list를 잘게 쪼개는 과정을 재귀적으로 반복하고, merge 함수를 사용하여 합쳐준다.
    # 코드를 작성하세요.
    return merge(merge_sort(left),merge_sort(right))



subin = [1, 3, 4, 5, 6, 10, 9, 13, 17, 19, 21, 20, 253, 251]
haerin = [2048, 1024, 3072, 5120, 4096]
print(merge_sort(subin))
print(merge_sort(haerin))
