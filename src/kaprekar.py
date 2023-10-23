# 获取所有三位数和四位数的转为卡布列克常数的推导过程
# author yunhu
# date 2023/10/5


def get_digit_from_small_to_large(digit):
    """
    获取一个数的从小到大排列, eg: 3756->3567

    Args:
        digit
    """
    small_to_large_digit = int(''.join(sorted(str(digit))))
    return small_to_large_digit


def get_digit_from_large_to_small(digit):
    """
    获取一个数的从大到小排列, eg: 1234->4321

    Args:
        digit
    """
    large_to_small_digit = int(''.join(sorted(str(digit), reverse=True)))
    return large_to_small_digit


def get_all_kaprekar_process(number):
    start_digit = 0
    end_digit = 0
    kaprekar_digit = 0
    if number == 3:
        start_digit = 100
        end_digit = 1000
        kaprekar_digit = 495
    elif number == 4:
        start_digit = 1000
        end_digit = 10000
        kaprekar_digit = 6174

    max_count = 0
    for digit in range(start_digit, end_digit):
        count = 1
        large_to_small_digit = get_digit_from_large_to_small(digit)
        small_to_large_digit = get_digit_from_small_to_large(digit)
        difference = large_to_small_digit - small_to_large_digit

        file_path = "./docs/" + str(number) + "_kaprekar.txt"

        file = open(file_path, "a", encoding="utf-8")
        file.write(str(digit) + "\n")
        file.write("第 " + str(count) + " 轮 " + "" + str(digit) + ": " +
                   str(large_to_small_digit) + " - " + str(small_to_large_digit) + " = " + str(difference) + "\n")

        # print(str(digit))
        # print("第 " + str(count) + " 轮 " + "" + str(digit) + ": " +
        #       str(large_to_small_digit) + " - " + str(small_to_large_digit) + " = " + str(difference))

        while difference != 0 and difference != kaprekar_digit:
            old_difference = difference
            large_to_small_digit = get_digit_from_large_to_small(difference)
            small_to_large_digit = get_digit_from_small_to_large(difference)
            difference = large_to_small_digit - small_to_large_digit
            count = count + 1
            if count > max_count:
                max_count = count

            file.write("第 " + str(count) + " 轮 " + str(old_difference) + ": " +
                       str(large_to_small_digit) + " - " + str(small_to_large_digit) + " = " + str(difference) + "\n")
            # print("第 " + str(count) + " 轮 " + str(old_difference) + ": " +
            #       str(large_to_small_digit) + " - " + str(small_to_large_digit) + " = " + str(difference))

        # print("\n")
        file.write("\n")
    print(str(max_count))


if __name__ == "__main__":
    get_all_kaprekar_process(3)
    get_all_kaprekar_process(4)
