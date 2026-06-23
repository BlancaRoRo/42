/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 14:03:35 by blromero          #+#    #+#             */
/*   Updated: 2026/05/07 16:01:18 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_atoi(const char *nptr)
{
	int	resultado;
	int	index;
	int	signo;

	signo = 1;
	index = 0;
	resultado = 0;
	while ((nptr[index] >= 9 && nptr[index] <= 13) || nptr[index] == 32)
		index++;
	if (nptr[index] == '-' || nptr[index] == '+')
	{
		if (nptr[index] == '-')
			signo = -1;
		index++;
	}
	while (nptr[index] >= '0' && nptr[index] <= '9')
	{
		resultado = (resultado * 10) + (nptr[index] - '0');
		index++;
	}
	return (resultado * signo);
}
