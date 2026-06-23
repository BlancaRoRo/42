/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putbase.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/14 11:55:07 by blromero          #+#    #+#             */
/*   Updated: 2026/06/22 15:41:40 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

void	ft_putbase(unsigned long long n, char *base)
{
	size_t	len;

	if (!base)
		return ;
	len = ft_strlen(base);
	if (n >= len)
		ft_putbase(n / len, base);
	write (1, &base[n % len], 1);
}
