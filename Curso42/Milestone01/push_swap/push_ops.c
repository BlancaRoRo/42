/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_ops.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 12:45:38 by blromero          #+#    #+#             */
/*   Updated: 2026/07/19 12:41:31 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	lst_length(t_stack *a)
{
	int	index;
	t_stack	*tmp;

	tmp = a;
	index = 0;
	while (tmp)
	{
		tmp = tmp->next;
		index++;
	}
	return (index);
}

void	pa(t_stack **a, t_stack **b, t_stats *s)
{
	t_stack *tmp;

	if (!*b)
		return ;
	tmp = *b;
	*b = (*b)->next;
	tmp->next = *a;
	*a = tmp;
	if (s->bench == 1)
		s->pa += 1;
	else
		write(1, "pa\n", 3);
}

void	pb(t_stack **a, t_stack **b, t_stats *s)
{
	t_stack *tmp;
	if (!*a)
		return ;
	tmp = *a;
	*a = (*a)->next;
	tmp->next = *b;
	*b = tmp;
	if (s->bench == 1)
		s->pb +=1;
	else 
		write(1, "pb\n", 3);
}
