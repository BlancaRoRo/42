/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate_ops.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 16:12:28 by blromero          #+#    #+#             */
/*   Updated: 2026/07/04 16:41:28 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ra(t_stack **a)
{
	t_stack *primero;
	t_stack	*ultimo;

	if ( !*a || lst_length(*a) == 1)
		return ;
	primero = *a;
	ultimo = *a;
	while (ultimo->next)
		ultimo = utlimo->next;
	*a = primero->next;
	ultimo->next = primero;
	primero->next = NULL;
}

void	rb(t_stack **b)
{
	t_stack	*primero;
	t_stack	*ultimo;

	if (!*b || lst_length(*b) == 1)
		return ;
	primero = *b;
	ultimo = *b;
	while (ultimo->next)
		ultimo = ultimo->next;
	*b = primero->next;
	ultimo->next = primero;
	primero->next = NULL;
}

void	rr(t_stack **a, t_stack **b)
{
	ra(a);
	rb(b);
}
