/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rrotate_ops.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 16:41:36 by blromero          #+#    #+#             */
/*   Updated: 2026/07/19 12:37:02 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rra_b(t_stack **a)
{
	t_stack	*primero;
	t_stack *ultimo;
	t_stack *final;

	if (!*a || lst_length(*a) == 1)
		return ;
	primero = *a;
	ultimo = *a;
	final = *a;
	while (ultimo->next)
		ultimo = ultimo->next;
	*a = ultimo;
	ultimo->next = primero;
	while (final->next != ultimo)
		final = final->next;
	final->next = NULL;
}

void	rrb_b(t_stack **b)
{
	t_stack	*primero;
	t_stack	*penultimo;
	t_stack	*ultimo;

	if (!*b || lst_length(*b) == 1)
		return ;
	primero = *b;
	penultimo = *b;
	while (penultimo->next->next)
		penultimo = penultimo->next;
	ultimo = penultimo->next;
	ultimo->next = primero;
	*b = ultimo;
	penultimo->next = NULL;
}

void	rra(t_stack **a, t_stats *s)
{
	rra_b(a);
	if (s->bench)
		s->rra += 1;
	else
		write(1, "rra\n", 4);
}

void	rrb(t_stack **b, t_stats *s)
{
	rrb_b(b);
	if (s->bench)
		s->rrb += 1;
	else 
		write(1, "rrb\n", 4);
}
void	rrr(t_stack **a, t_stack **b, t_stats *s)
{
	rra_b(a);
	rrb_b(b);
	if (s->bench)
		s->rrr += 1;
	else 
		write(1, "rrr\n", 4);
}
