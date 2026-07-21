/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate_ops.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 16:12:28 by blromero          #+#    #+#             */
/*   Updated: 2026/07/19 12:36:10 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ra_b(t_stack **a)
{
	t_stack *primero;
	t_stack	*ultimo;

	if ( !*a || lst_length(*a) == 1)
		return ;
	primero = *a;
	ultimo = *a;
	while (ultimo->next)
		ultimo = ultimo->next;
	*a = primero->next;
	ultimo->next = primero;
	primero->next = NULL;

}

void	rb_b(t_stack **b)
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

void	ra(t_stack **a, t_stats *s)
{
	ra_b(a);
	if (s->bench)
		s->ra +=1;
	else 
		write(1, "ra\n", 3);
}

void	rb(t_stack **b, t_stats *s)
{
	rb_b(b);
	if (s->bench)
		s->rb += 1;
	else
		write(1, "rb\n", 3);
}
void	rr(t_stack **a, t_stack **b, t_stats *s)
{
	ra_b(a);
	rb_b(b);
	if (s->bench)
		s->rr += 1;
	else 
	write(1, "rr\n", 3);
}
