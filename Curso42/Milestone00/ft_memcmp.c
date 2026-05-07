/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 13:17:39 by blromero          #+#    #+#             */
/*   Updated: 2026/05/07 12:44:24 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	const unsigned char	*st1;
	const unsigned char	*st2;
	size_t				index;

	index = 0;
	st1 = s1;
	st2 = s2;
	while (index < n)
	{
		if (st1[index] != st2[index])
			return (st1[index] - st2[index]);
		index++;
	}
	return (0);
}
