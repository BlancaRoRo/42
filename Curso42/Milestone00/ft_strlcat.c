/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 10:36:14 by blromero          #+#    #+#             */
/*   Updated: 2026/05/07 15:34:06 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t dsize)
{
	size_t	lsrc;
	size_t	ldst;
	size_t	i;

	i = 0;
	lsrc = ft_strlen(src);
	ldst = ft_strlen(dst);
	if (dsize <= ldst)
		return (lsrc + dsize);
	while (src[i] != '\0' && (ldst + i + 1) < dsize)
	{
		dst[ldst + i] = src[i];
		i++;
	}
	dst[ldst + i] = '\0';
	return (ldst + lsrc);
}
