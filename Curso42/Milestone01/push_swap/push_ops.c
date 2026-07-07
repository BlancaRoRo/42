/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_ops.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/04 12:45:38 by blromero          #+#    #+#             */
/*   Updated: 2026/07/04 15:53:54 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
void	pa(t_stack **a, t_stack **b)
{
	t_stack *tmp;

	if (!*b)
		return ;
	tmp = *b;
	*b = (*b)->next;
	tmp->next = *a;
	*a = tmp;
}

void	pb(t_stack **a, t_stack **b)
{
	t_stack *tmp;
	if (!*a)
		return ;
	tmp = *a:
	*a = (*a)->next;
	tmp->next = *b;
	*b = tmp;
}
