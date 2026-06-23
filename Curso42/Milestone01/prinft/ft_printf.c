/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/12 20:35:01 by blromero          #+#    #+#             */
/*   Updated: 2026/06/22 16:35:53 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	selector(va_list ap, char format)
{
	if (format == 'c')
	{
		ft_putchar_fd(va_arg(ap, int), 1);
		return (1);
	}
	else if (format == 'd' || format == 'i')
		return (ft_putint_print(va_arg(ap, int)));
	else if (format == 's')
		return (ft_putstr_print(va_arg(ap, char *)));
	else if (format == 'p')
		return (ft_putvoid_print(va_arg(ap, void *)));
	else if (format == 'u')
		return (ft_putunsigned_print(va_arg(ap, int)));
	else if (format == 'x')
		return (ft_puthex_print(va_arg(ap, int), "0123456789abcdef"));
	else if (format == 'X')
		return (ft_puthex_print(va_arg(ap, int), "0123456789ABCDEF"));
	else if (format == '%')
	{
		write(1, "%", 1);
		return (1);
	}
	return (0);
}

int	ft_printf(char const *format, ...)
{
	va_list	ap;
	int		index;
	int		count;

	index = 0;
	count = 0;
	va_start(ap, format);
	while (format[index])
	{
		if (format[index] == '%')
		{
			count += selector(ap, format[index + 1]);
			index += 2;
		}
		else
		{
			write(1, &format[index], 1);
			count++;
			index++;
		}
	}
	va_end(ap);
	return (count);
}
