/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   alg_complex_adap.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/13 17:40:22 by blromero          #+#    #+#             */
/*   Updated: 2026/07/20 15:08:03 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	get_bit(int	nbr, int position)
{
	return ((nbr >> position) & 1);
}
int	count_bits(t_stack **a)
{
	int	max;
	int	bits;
	int	min;

	bits = 0;
	get_max(*a, &max);
	get_min(*a, &min);
	while (((max - min) >> bits) > 0)
		bits++;
	return (bits);
}
void	relocating(t_stack **a, t_stack **b, t_stats *s)
{
	int	size;
	int	index;

	index = 0;
	size = lst_length(*b);
	while (index < size)
	{
		pa(a, b, s);
		index++;
	}
	while (0 < size)
	{
		ra(a, s);
		size--;
	}
}
void	complex(t_stack **a, t_stack **b, t_stats *s)
{
	int	max_bits;
	int	bit_pos;
	int	i;
	int	size;
	int	min;

	i = 0;
	size = lst_length(*a);
	bit_pos = 0;
	max_bits = count_bits(a);
	get_min(*a, &min);
	while (bit_pos < max_bits)
	{
		while (i < size)
		{
			if(get_bit((*a)->value - min, bit_pos) > 0)
				pb(a, b, s);
			else
				ra(a, s);
			i++;
		}
		i = 0;
		relocating(a,b, s);
		bit_pos++;
	}
}

void	adaptive(float disorder, t_stack **a, t_stack **b, t_stats *s)
{
	if (disorder == 0)
		return ;
	if (disorder > 0 && disorder < 0.2)
	{
		simple_n_ab(a, s, 1);
		return ;
	}
	if (disorder >= 0.2 && disorder < 0.5)
	{
		medium(a, b, s);
		return ;
	}
	if (disorder >= 0.5)
	{
		complex(a, b, s);
		return ;
	}
}
