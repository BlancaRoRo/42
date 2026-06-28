NAME = get_next_line.a
CC = cc
CFLAGS = -Wall -Wextra -Werror -D BUFFER_SIZE=42
AR = ar rcs
RM = rm -rf

SRC = get_next_line.c get_next_line_utils.c 
all:$(NAME)
OBJ = $(SRC:.c=.o)
$(NAME): $(OBJ) 
	$(AR) $(NAME) $(OBJ)

clean: 
	$(RM) $(OBJ)
fclean: clean
	$(RM) $(NAME)
re: fclean clean
.PHONY: all clean fclean re 
