def ft_count_harvest_recursive_helper(days):
    if days < 1:
        return
    ft_count_harvest_recursive_helper(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count_harvest_recursive_helper(days)
    print("Harvest time!")
