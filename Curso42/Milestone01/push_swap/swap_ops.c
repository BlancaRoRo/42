/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_ops.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 13:06:08 by blromero          #+#    #+#             */
/*   Updated: 2026/07/19 12:37:50 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
void	sa_b(t_stack **a)
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

void	sb_b(t_stack **b)
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
	*b = segundo;
}

void	sa(t_stack **a, t_stats *s)
{
	sa_b(a);
	if (s->bench)
		s->sa += 1;
	else
		write(1, "sa\n", 3);
}

void	sb(t_stack **b, t_stats *s)
{
	sb_b(b);
	if (s->bench)
		s->sb += 1;
	else 
		write(1, "sb\n", 3);
}

void	ss(t_stack **a, t_stack **b, t_stats *s)
{
	if (!*a || !*b)
		return ;
	sb_b(b);
	sa_b(a);
	if (s->bench)
		s->ss += 1;
	else 
		write(1, "ss\n", 3);
}
