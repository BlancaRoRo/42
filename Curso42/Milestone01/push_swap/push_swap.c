/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/02 18:33:58 by blromero          #+#    #+#             */
/*   Updated: 2026/07/20 18:43:13 by blromero         ###   ########.fr       */
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
	while (a != NULL && a->next != NULL)
	{
		b = a->next;
		while (b !=  NULL)
		{
			total_pairs++;
			if (a->value > b->value)
				mistakes++;
			b = b->next;
		}
		a = a->next;
	}
	return ((float)mistakes / (float)total_pairs);
}

void	push_swap(t_stack **a, t_stack **b, int algorithm, float disorder, t_stats *s)
{
	if (s->bench == 1)
		init_stats(s);
	if (algorithm == 1)
		simple(a, b, s);
	if (algorithm == 2)
		medium(a, b, s);
	if (algorithm == 3)
		complex(a, b, s);
	else
		adaptive(disorder, a, b, s);
}
int main(int argc, char **argv){

	t_stack	*b;
	t_stack	*a;
	t_stats	s;

	int	algorithm;
	int	start;
	float	disorder;

	if (argc < 2)
		return (0);
	b = NULL;
	start = 0;
	algorithm = 0;
	if (!parse_flags(argc, argv, &algorithm, &s, &start) || !data_check(argv, start))
	{
		write(2, "Error\n", 6);
		return (1);
	}
	a = fill_stack(argv, start);
	if (!a || !has_duplicate(a))
	{
		write(2 ,"Error\n" ,6);
		return (1);
	}
	disorder = compute_disorder(a);
	push_swap(&a, &b, algorithm, disorder, &s);
	if (s.bench)
	print_bench(&s, disorder);
/*	while (a)
	{
		printf("%i", a->value);
		a = a->next;
	}
	write(1, "\n", 1);*/
	return (0);
}
