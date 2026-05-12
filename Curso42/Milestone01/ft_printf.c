/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/12 20:35:01 by blromero          #+#    #+#             */
/*   Updated: 2026/05/12 21:17:20 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libftprintf"
#include <stdarg.h>
#include <stdio.h>

int	ft_printf(char const *format, ...)
{	
	va_list	ap;
	int	index;

	index = 0;
	ap = 
	while (format[index])
	{
		if (format[index] == '%')
		{
			selector(format[index + 1]);
			
		}
		write(1, &format[index], 1);
		index++;
	}
}
