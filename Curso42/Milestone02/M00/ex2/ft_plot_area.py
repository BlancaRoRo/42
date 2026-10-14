def ft_plot_area():
    length = int(input("Enter length: "))
    # input() returns a str. You must cast/convert these variables
    # to do math operations.
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
