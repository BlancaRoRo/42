/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/20 18:02:27 by blromero          #+#    #+#             */
/*   Updated: 2026/06/22 15:59:46 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	ft_putint_print(int c)
{
	unsigned long	l;

	ft_putnbr_fd(c, 1);
	l = c;
	if (c < 0)
		return (ft_count_digit(-l, 10) + 1);
	return (ft_count_digit(l, 10));
}

int	ft_putstr_print(char *s)
{
	if (!s)
	{
		write(1, "(null)", 6);
		return (6);
	}
	ft_putstr_fd(s, 1);
	return (ft_strlen(s));
}

int	ft_putvoid_print(void *p)
{
	if (!p)
	{
		write(1, "(nil)", 5);
		return (5);
	}
	write(1, "0x", 2);
	ft_putbase((unsigned long long)p, "0123456789abcdef");
	return (2 + ft_count_digit((unsigned long long)p, 16));
}

int	ft_putunsigned_print(unsigned int c)
{
	ft_putbase(c, "0123456789");
	return (ft_count_digit(c, 10));
}

int	ft_puthex_print(unsigned int c, char *base)
{
	ft_putbase(c, base);
	return (ft_count_digit(c, 16));
}
