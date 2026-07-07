/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 10:16:26 by blromero          #+#    #+#             */
/*   Updated: 2026/04/21 10:35:47 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcpy(char *dest, const char *src, size_t dsize)
{
	size_t	lsrc;
	size_t	index;

	index = 0;
	lsrc = ft_strlen(src);
	if (dsize <= 0)
		return (lsrc);
	while (1 < dsize && src[index] != '\0')
	{
		dest[index] = src[index];
		index++;
		dsize--;
	}
	dest[index] = '\0';
	return (lsrc);
}
