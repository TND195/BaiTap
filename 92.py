#Bài 92: Tìm ước số chung lớn nhất của 2 số nguyên dương

#comment?
def is_number(value):
    return value.isdigit() == False or float(value).is_integer() == False or int(value) <= 0

# comment? 
def find_greatest_common_divisor(first ,second):
    # comment xu ly 
    if first > second:
        target_number = second
    else:
        target_number = first
    for i in range(target_number, 1, -1):
        if first % i ==0 and second % i ==0:
            return i
            #break ? return break làm gì? 

if __name__ == '__main__':
    # comment xu ly
    first_number = (input("Nhập số thứ nhất "))
    while is_number(first_number) == False:
        first_number = (input("Nhập lại số thứ nhất "))
    second_number = (input("Nhập số thứ hai "))
    while is_number(first_number) == False:
        first_number = (input("Nhập lại số thứ hai "))
    print("Ước chung lớn nhất của 2 số là " + str(find_greatest_common_divisor(int(first_number),int(second_number))))
