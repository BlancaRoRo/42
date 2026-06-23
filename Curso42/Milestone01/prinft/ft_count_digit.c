/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_count_digit.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/20 12:24:00 by blromero          #+#    #+#             */
/*   Updated: 2026/06/21 16:09:31 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	ft_count_digit(unsigned long long n, int base_len)
{
	int	index;

	index = 0;
	if (base_len < 0)
		return (0);
	if (n == 0)
		return (1);
	while (n > 0)
	{
		n = n / base_len;
		index++;
	}
	return (index);
}
