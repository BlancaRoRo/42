/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algorithm.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 16:57:00 by blromero          #+#    #+#             */
/*   Updated: 2026/07/09 13:31:55 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	simple(t_stack **a)
{
	int	index;
	int	size;

	index = 0;
	size = ft_lstlength(a);
	while (index < size)
	{	
		if (!(*a) || !(*a)->next)
			return ;
		if ((*a)->value < siguiente->value)
		{
			sa(a)
			index = 0;
		}
		ra(a);
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

void	medium(t_stack **a, t_stack **b)
{
	int	min;
	int	max;
	int	length;
	t_stack	*franja1;
	t_stack	*franja2;
	t_stack	*franja3;

	min = INT_MAX;
	max = INT_MIN;
	get_min_max(*a, &min, &max);
	length = (max + min - 1) / 3;
	sort_range(min, min + length - 1, b, a);
	sort_range(min + length, (length +  min) * 2 - 1, b, a);
	sort_range((min + length * 2), max, b, a);
}

