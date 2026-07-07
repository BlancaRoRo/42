/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rrotate_ops.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 16:41:36 by blromero          #+#    #+#             */
/*   Updated: 2026/07/04 16:56:29 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rra(t_stack **a)
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

void	rrb(t_stack **b)
{
	t_stack	*primero;
	t_stack	*penultimo;
	t_stack	*ultimo;

	if (!*b || lst_length(*b) == 1)
		return ;
	primero = *a;
	penultimo = *a;
	while (penultimo->next->next)
		penultimo = penultimo->next;
	ultimo = penultimo->next;
	ultimo->next = primero;
	a* = ultimo;
	penultimo->next = NULL;

}

void	rrr(t_stack **a, t_stack **b)
{
	rra(a);
	rrb(b);

}
