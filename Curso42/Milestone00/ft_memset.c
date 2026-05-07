/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 20:02:41 by blromero          #+#    #+#             */
/*   Updated: 2026/05/07 12:48:33 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	size_t			index;
	unsigned char	*p;

	p = (unsigned char *) s;
	index = 0;
	while (index < n)
	{
		p[index] = (unsigned char) c;
		index++;
	}
	return (s);
}
