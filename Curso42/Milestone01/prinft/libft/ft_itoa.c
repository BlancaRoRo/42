/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 20:51:15 by blromero          #+#    #+#             */
/*   Updated: 2026/04/22 21:55:59 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static int	ft_len_int(long n)
{
	int	len;

	len = 0;
	if (n <= 0)
		len++;
	if (n < 0)
		n *= -1;
	while (0 < n)
	{
		n = n / 10;
		len++;
	}
	return (len);
}

char	*ft_itoa(int n)
{
	char	*p;
	int		len;
	long	digit;

	digit = n;
	len = ft_len_int(n);
	p = malloc(len + 1);
	if (!p)
		return (NULL);
	p[len] = '\0';
	if (digit == 0)
		p[0] = '0';
	if (digit < 0)
	{
		digit *= -1;
		p[0] = '-';
	}
	while (digit > 0)
	{
		p[len - 1] = digit % 10 + '0';
		digit /= 10;
		len--;
	}
	return (p);
}
