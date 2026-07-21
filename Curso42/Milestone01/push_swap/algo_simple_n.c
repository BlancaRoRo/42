/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_simple_n.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/20 12:43:19 by blromero          #+#    #+#             */
/*   Updated: 2026/07/20 14:48:03 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rotation(int *j, t_stack **ab, t_stats *s, int flag)
{
	while (*j > 0)
	{
		if (flag)
			rra(ab, s);
		else 
			rrb(ab, s);
		(*j)--;
	}
}
void	simple_sort(int *j, t_stack **ab, int *swapped, t_stats *s, int	flag)
{
	int	size;

	size = lst_length(*ab);
	while (*j < size - 1)
	{
		if ((*ab)->value > (*ab)->next->value)
		{
			if (flag)
				sa(ab, s);
			else
				sb(ab, s);
			*swapped = 1;
		}
		(*j)++;
		if (flag)
			ra(ab, s);
		else
			rb(ab, s);
	}

}
void	simple_n_ab(t_stack **a, t_stats *s, int flag)
{
	int	passes;
	int	j;
	int	i;
	int	swapped;

	passes = 3;
	i = 0;
	swapped = 0;
       while (i < passes)
	{
		j = 0;
		simple_sort(&j, a, &swapped, s, flag);
		rotation(&j, a, s, flag);
		if (!swapped)
			break;
		i++;
	 }
}

