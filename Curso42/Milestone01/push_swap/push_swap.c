/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/02 18:33:58 by blromero          #+#    #+#             */
/*   Updated: 2026/07/05 12:46:24 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

float	compute_disorder(t_stack *a)
{
	size_t	mistakes;
	size_t	total_pairs;
	t_stack	*b;

	if (a == NULL || a->next == NULL)
		return (0);
	mistakes = 0;
	total_pairs = 0;
	while (a == NULL && a->next != NULL)
	{
		b = a->next;
		while (b ==  NULL)
		{
			total_pairs++;
			if (a->value > b->value)
				mistakes++;
			b = b->next;
		}
		a = a->next;
	}
	return (mistakes / total_pairs);
}

t_stack	**push_swap(t_stack **a, t_stack **b, int algorithm)
{
	if (algortihm == 0)
		return (simple(a));
}
int main(int argc, char **argv){

	t_stack	*b;
	t_stack	*a;

	int	algorithm;
	int	start;

	if (argc < 2)
		return (0);
	b = NULL;
	start = 1;
	algorithm = is_algorithm(argv[1]); 
	if (algorithm >= 0)
		start = 2;
	
	if (!data_check(argv, start))
	{
		write(2 ,"Error\n" ,6);
		return (1);
	}
	a = fill_stack(argv, start);
	if (!a || !has_duplicate(a))
	{
		write(2 ,"Error\n" ,6);
		return (1);
	}
	
	return (0);
}
