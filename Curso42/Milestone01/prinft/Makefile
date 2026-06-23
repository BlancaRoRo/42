NAME = libftprintf.a
CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -rf 

LIBFT_DIR = ./libft
LIBFT	= $(LIBFT_DIR)/libft.a

SRC	=  ft_put.c ft_count_digit.c ft_putbase.c ft_printf.c

OBJ = $(SRC:.c=.o)

all:$(NAME)

$(NAME): $(OBJ) $(LIBFT)
	@cp $(LIBFT) $(NAME)
	$(AR) $(NAME) $(OBJ)

$(LIBFT):
	@make -C $(LIBFT_DIR)

%.o: %.c
	$(CC) $(CFLAGS) -I$(LIBFT_DIR) -c $< -o $@
clean:
	$(RM) $(OBJ) 
	@make -C $(LIBFT_DIR) clean
fclean:
	$(RM) $(NAME)
	@make -C $(LIBFT_DIR) fclean
re: fclean all

.PHONY: all clean fclean re
