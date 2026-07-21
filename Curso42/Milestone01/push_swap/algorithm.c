/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algorithm.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 16:57:00 by blromero          #+#    #+#             */
/*   Updated: 2026/07/21 09:01:44 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <math.h>
void	print_stack(char *s ,t_stack **a)
{
	t_stack *tmp;

	tmp = *a;
	printf("%s : ", s);
	while(tmp)
	{
		printf("%i", tmp->value);
		tmp = tmp->next;
	}
	printf("\n");
}
void	get_min(t_stack *a, int *min)
{
	*min = a->value;
	while (a)
	{
		if (a->value < *min)
			*min = a->value;
		a = a->next;
	}
}
void    sort_range(int range_min, int range_max, stack *b, stack *a )
{
	while (a->next)
	{
		if (range_min <= a->value && range_max >= a->value)
			pb(a,b);
		else
			ra(a);
	}
	simple(b);
        while (b)
	{
		pa(a,b);
		ra(a);
	}
}

void	get_max(t_stack *a, int *max)
{
	*max = a->value;
	while (a)
	{
		if (a->value > *max)
			*max = a->value;
		a = a->next;
	}
}

void	sort_range( int range_min, int range_max, t_stack **a, t_stack **b, t_stats *s)
{
	t_stack *aux;
	int	i;
	int	size;

	size = lst_length(*a);
	aux = NULL;
	i = 0;
	while (i < size)
	{
		if ((*a)->value <= range_max && (*a)->value >= range_min)
			pb(a, b, s);
		else
			ra(a, s);
		i++;
	}
	simple_n_ab(b, s, 0);
	while (*b)
	{
		pa(a, b, s);
		ra(a, s);
	}
}

void	simple (t_stack **a, t_stack **b, t_stats *s)
{
	int	index;
	int	size;
	int	min;

	size = lst_length(*a);
	index = 0;
	
	while (index < size)
	{
		get_min(*a, &min);
		while((*a)->value != min)
			ra(a, s);
		pb(a, b, s);
		index++;
	}
	index = 0;
	while (index < size)
	{
		pa(a, b, s);
		index++;
	}
}
void	medium(t_stack **a, t_stack **b, t_stats *s)
{
	int	min;
	int	max;
	int	length;

	get_min(*a, &min);
	get_max(*a, &max);
	length = (max - min + 1 + 2) / 3;
	sort_range(min, length - 1 + min, a, b, s);
	sort_range(length + min, length * 2 - 1 + min, a, b, s);
	sort_range(length * 2 + min, max, a ,b, s);
}
