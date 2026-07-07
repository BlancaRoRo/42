/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_ops.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 13:06:08 by blromero          #+#    #+#             */
/*   Updated: 2026/07/04 16:12:17 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
int	lst_length(t_stack *a)
{
	int	index;

	index = 0;
	while (a)
	{
		a = a->next;
		index++;
	}
	return (index);
}

void	sa(t_stack **a)
{
	int	size;
	t_stack	*primero;
	t_stack *segundo;

	size = lst_length(*a);
	if (size < 2)
		return ;
	primero = *a;
	segundo = (*a)->next;
        primero->next = segundo->next;
	*a = segundo;
	segundo->next = primero;
	*a = segundo;
}

void	sb(t_stack **b)
{
	int	size;
	t_stack *primero;
	t_stack *segundo;
	size = lst_length(*b);
	if (size < 2)
		return ;
	primero = *b;
	segundo = (*b)->next;
	primero->next = segundo->next;
	segundo->next = primero;
	b* = segundo;
}
void	ss(t_stack **a, t_stack **b)
{
	if (!*a || !*b)
		return ;
	sb(b);
	sa(a);
}
