/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 13:04:07 by blromero          #+#    #+#             */
/*   Updated: 2026/05/06 20:00:14 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t				index;
	const unsigned char	*temp;

	temp = s;
	index = 0;
	while (n > index)
	{
		if (temp[index] == (unsigned char) c)
			return ((void *)&temp[index]);
		index++;
	}
	return (NULL);
}
