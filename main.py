def sort_and_print(lst):
    print("Asl ro'yxat: ", lst)
    sorted_lst_asc = sorted(lst)
    sorted_lst_desc = sorted_lst_asc[::-1]
    print("Ro'yxat o'sish tartibida: ", sorted_lst_asc)
    print("Ro'yxat kamayish tartibida: ", sorted_lst_desc)

def main():
    lst1 = [64, 34, 25, 12, 22, 11, 90]
    lst2 = [5, 2, 8, 1, 9]
    lst3 = [10, 7, 3, 6, 4]

    print("1-ro'yxat: ")
    sort_and_print(lst1)

    print("\n2-ro'yxat: ")
    sort_and_print(lst2)

    print("\n3-ro'yxat: ")
    sort_and_print(lst3)

    lst4 = [15, 20, 10, 30, 25]
    print("\n4-ro'yxat: ")
    sort_and_print(lst4)

    lst5 = [100, 50, 75, 25, 1000]
    print("\n5-ro'yxat: ")
    sort_and_print(lst5)

    lst6 = [1, 2, 3, 4, 5]
    print("\n6-ro'yxat: ")
    sort_and_print(lst6)

    lst7 = [10, 9, 8, 7, 6]
    print("\n7-ro'yxat: ")
    sort_and_print(lst7)

    lst8 = [5, 5, 5, 5, 5]
    print("\n8-ro'yxat: ")
    sort_and_print(lst8)

    lst9 = [-1, -2, -3, -4, -5]
    print("\n9-ro'yxat: ")
    sort_and_print(lst9)

    lst10 = [-10, -9, -8, -7, -6]
    print("\n10-ro'yxat: ")
    sort_and_print(lst10)

if __name__ == "__main__":
    main()