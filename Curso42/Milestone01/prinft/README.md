*This project was created by Blromero as part of the 42 curriculum.*

---

# Description
This project is a personal recreation of the standard C function `printf`. It prints text to the terminal and handles various format specifiers and symbols. However, it uses a different structural approach, leveraging a few functions from a previous project (`Libft`), and does not implement the buffer management found in the original `printf`.

## Files

### ft_printf.c
This file contains two distinct functions: the+ main `printf` implementation and the format `selector`.

*   **`ft_printf`:** Writes characters and symbols to the output and calls the selector to handle different formats (e.g., `%p`, `%i`, `%d`, `%u`).
*   **`ft_selector`:** Determines which function to call based on the format specifier received from `ft_printf`.

---

### ft_put.c
Every function in this file returns the total number of characters written, calculated by `ft_count_digit`.

*   **`ft_putint_print`:** Handles the conversion from `int` to `long` and prints the sign if necessary. It calls `ft_putbase` to print the number in decimal format and `ft_count_digit` to count the written digits.
*   **`ft_putstr_print`:** Prints `(null)` if the string pointer is null. Otherwise, it calls `ft_putstr_fd` from `Libft` to output the string.
*   **`ft_putvoid_print`:** Prints `(nil)` if the pointer is null. Otherwise, it converts the memory address into an `unsigned long`, then calls `ft_putbase` and `ft_count_digit` to print the address in hexadecimal and count the characters.
*   **`ft_putunsigned_print`:** Calls `ft_putbase` to print the number in decimal format and returns the count from `ft_count_digit`.
*   **`ft_puthex_print`:** Receives the base (uppercase or lowercase) used to print the number, calls `ft_putbase` to output it, and returns the result of `ft_count_digit`.

---

### ft_putbase.c
*   **`ft_putbase`:** Prints the number to the terminal based on the specific base it receives.

---

### ft_count_digit.c
*   **`ft_count_digit`:** Counts the total number of digits of the received number, calculated using the length of the base used for conversion.

---

The remaining functions used in this project come from `Libft`: `ft_putstr_fd`, `ft_putchar_fd`, and `ft_putnbr_fd`. To learn more about them, you can check the `Libft` README.md in the `/Libft` directory.

---

## Library

### ft_printf.h
Contains all function prototypes and the standard libraries required by the project.

## Program
### libftprintf.a
The static library compiled by the Makefile.

## Makefile
It compiles the program along with all the required `Libft` functions.  
The flags configured are: `-Wall -Wextra -Werror`

---

# Instructions
To use this project, simply clone or download the repository. All libraries and dependencies are already included.

Compile the project using the following Makefile commands:
*   To compile: `make`
*   To remove object files (`.o`): `make clean`
*   To remove object files and the compiled library (`.a`): `make fclean`
*   To recompile from scratch: `make re`

# Resources
A lot of time and effort and, for sure: 
## Required Libraries
`<stdio.h>` | `<stdarg.h>` | `<unistd.h>`
