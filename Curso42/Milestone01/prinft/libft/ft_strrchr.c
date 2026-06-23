/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 11:30:41 by blromero          #+#    #+#             */
/*   Updated: 2026/05/06 19:08:37 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int	ls;

	ls = ft_strlen(s);
	while (ls >= 0)
	{
		if (s[ls] == (char)c)
			return ((char *)s + ls);
		ls--;
	}
	return (NULL);
}
