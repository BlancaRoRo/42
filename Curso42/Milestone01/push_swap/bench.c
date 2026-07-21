/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/20 17:07:51 by blromero          #+#    #+#             */
/*   Updated: 2026/07/20 18:47:40 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	init_stats(t_stats *s)
{
	s->pa = 0;
	s->pb = 0;
	s->sa = 0;
	s->sb = 0;
	s->ss = 0;
	s->ra = 0;
	s->rb = 0;
	s->rr = 0;
	s->rra = 0;
	s->rrb = 0;
	s->rrr = 0;
}

void	print_algorithm(float disorder)
{
	if (disorder == 0)
		return ;
	if (disorder > 0 && disorder < 0.2)
		write(1, "strategy: Adaptive / O(n)\n", 26);
	if (disorder >= 0.2 && disorder < 0.5)
		write(1, "strategy: Adapative / O(n√n)\n", 28);
	if (disorder >= 0.5)
		write(1, "strategy: Adaptive / O(nlog(n))\n",32);
}
void	print_bench(t_stats *s, float disorder)
{
	float	disorder_ptg;
	int	total_ops;

	total_ops = 0;
	disorder_ptg = (disorder * 100);
	printf("disorder: %f\n", disorder_ptg);
	print_algorithm(disorder);
	total_ops =s->sa + s->sb + s->ss + s->pa + s->pb;
	total_ops += s->ra + s->rb + s->rr + s->rra + s->rrb + s->rrr;
	printf("total_ops: %i\n", total_ops);
	printf("sa: %i sb: %i ss: %i pa: %i pb: %i\n ra: %i rb: %i rr: %i rra: %i rrb: %i rrr: %i\n", 
			s->sa, s->sb, s->ss, s->pa, s->pb, s->ra, s->rb, s->rr, s->rra, s->rrb, s->rrr);

}
