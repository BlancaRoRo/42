
#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include <stdlib.h>
# include "./libft/libft.h"
# include <limits.h>

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
void		simple(t_stack **a);
void	sort_range(int range_min, int range_max, t_stack *b, t_stack  *a);
void	medium(t_stack **a, t_stack **b);
void	ra(t_stack **a);
void	rb(t_stack **b);
void	rr(t_stack **a, t_stack **b);
int	ft_strcmp(char *s1, char *s2);
int	is_algorithm(char *argv);
void	pa(t_stack **a, t_stack **b);
void	pb(t_stack **a, t_stack **b);
void	rra(t_stack **a);
void	rrb(t_stack **b);
void	rrr(t_stack **a, stack **b);
int	lst_length(t_stack *a);
void	sa(t_stack **a);
void	sb(t_stack **b);
void	ss(t_stack **a, t_stack **b);
#endif
