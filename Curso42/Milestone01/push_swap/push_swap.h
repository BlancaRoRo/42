
#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include <stdlib.h>
# include <limits.h>
# include "./libft/libft.h"
# include <stdio.h>

typedef struct s_stack
{
	int 		value;
	struct s_stack	*next;
}t_stack;

typedef	struct	s_stats
{
	int	bench;
	int	sa;
	int	sb;
	int	ss;
	int	pa;
	int	pb;
	int	ra;
	int	rb;
	int	rr;
	int	rra;
	int	rrb;
	int	rrr;
}t_stats;

void	init_stats(t_stats *s);
int		is_valid_number(char *s);
int		data_check(char **argv, int start);
int		has_duplicate(t_stack *a);
float	compute_disorder(t_stack *a);
int		is_algorithm(char *argv);
void	print_bench(t_stats *s, float disorder);
t_stack	*fill_stack(char **argv, int start);
int	parse_flags(int	argc, char **argv, int *algorithm, t_stats *s, int *start);
void	rra(t_stack **a, t_stats *s);
void	rrb(t_stack **b, t_stats *s);
void	rrr(t_stack **a, t_stack **b, t_stats *s);
int		lst_length(t_stack *a);
void	simple_n_ab(t_stack **a, t_stats *s, int flag);
void	sa(t_stack **a, t_stats *s);
void	sb(t_stack **b, t_stats *s);
void	ss(t_stack **a, t_stack **b, t_stats *s);
void	pa(t_stack **a, t_stack **b, t_stats *s);
void	pb(t_stack **a, t_stack **b, t_stats *s);
void	ra(t_stack **a, t_stats *s);
void	rb(t_stack **b, t_stats *s);
void	rr(t_stack **a, t_stack **b, t_stats *s);
int	ft_strcmp(char *s1, char *s2);
int	is_algorithm(char *argv);
void	simple(t_stack **a, t_stack **b, t_stats *s);
void	medium(t_stack **a, t_stack **b, t_stats *s);
void	get_max(t_stack *a, int *max);
void	complex(t_stack **a, t_stack **b, t_stats *s);
void	print_stack(char *s, t_stack **a);
void	adaptive(float disorder, t_stack **a, t_stack **b, t_stats *s);
void	get_min(t_stack *a, int	*min);

#endif
