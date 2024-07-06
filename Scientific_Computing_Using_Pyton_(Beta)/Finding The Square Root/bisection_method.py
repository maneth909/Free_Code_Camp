def square_root(target_num, tolerance=1e-7, iteration=100):
    if target_num < 0:
        raise ValueError('The number should not be less than zero')
    elif target_num == 0:
        root = 0
        print(f'The root of {target_num} is 0')
    elif target_num == 1:
        root = 1
        print(f'The root of {target_num} is 1')
    else:
        low = 0
        high = max(1, target_num)
        root = None

        for i in range(iteration):
            mid = (low+high) / 2
            square_mid = mid**2
            if abs(square_mid-target_num) < tolerance:
                root = mid
                break
            elif square_mid < target_num:
                low = mid
            else:
                high = mid
        
        if root is None:
            print(f"Failed to converge within {iteration} iterations.")
        else:
            print(f'Square root of {target_num} is approximately {root}')

    return root

N = 16
print(square_root(N))