/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 13:29:22 by blromero          #+#    #+#             */
/*   Updated: 2026/05/07 15:54:12 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t n)
{
	size_t	index;
	size_t	valor;

	index = 0;
	valor = 0;
	if (little[0] == '\0')
		return ((char *)big);
	while (big[index] != '\0' && n > index)
	{
		while (big[index + valor] == little[valor] && n > (index + valor))
		{
			if (little[valor + 1] == '\0')
				return ((char *)&big[index]);
			valor++;
		}
		valor = 0;
		index++;
	}
	return (NULL);
}
