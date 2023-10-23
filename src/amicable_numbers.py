# 获取前一百个亲和数
# author yunhu
# date 2023/10/23

def get_proper_divisor_sum(digit):
    """
    获取一个数真因子之和, eg: 32->[1, 2, 4, 8, 16]->31

    Args:
        digit 
    """
    # 1 是所有正整数的真因子之一
    proper_divisor_sum = 1
    for i in range(2, int(digit**0.5) + 1):
        if digit % i == 0:
            proper_divisor_sum += i
            # 避免重复计算相同的因子
            if i != digit // i:
                proper_divisor_sum += digit // i
    return proper_divisor_sum


if __name__ == "__main__":
    amicable_numbers_list = []
    count = 0
    for digit in range(10000000):
        # digit 的真因子之和
        first = get_proper_divisor_sum(digit)

        # first 的真因子之和
        second = get_proper_divisor_sum(first)
        if digit == second and digit != first:
            amicable_numbers_tuple = tuple(sorted([digit, first]))
            if amicable_numbers_tuple not in amicable_numbers_list:
                print(str(count))
                print(amicable_numbers_tuple)
                count = count + 1
                amicable_numbers_list.append(amicable_numbers_tuple)
    print(amicable_numbers_list)
