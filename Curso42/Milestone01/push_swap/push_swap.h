
#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include <stdlib.h>
# include "./libft/libft.h"

typedef struct s_stack
{
	int 		value;
	struct s_stack	*next;
}	t_stack;
int		is_valid_number(char *s);
int		data_check(char **argv, int start);
int		has_duplicate(t_stack *a);
float	compute_disorder(t_stack *a);
int		is_algorithm(char *argv);
t_stack	*fill_stack(char **argv, int start);

#endif
