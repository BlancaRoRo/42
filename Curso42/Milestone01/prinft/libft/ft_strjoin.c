/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 16:12:34 by blromero          #+#    #+#             */
/*   Updated: 2026/04/22 16:24:25 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*temp;
	size_t	lens1;
	size_t	lens2;

	if (!s1 || !s2)
		return (NULL);
	lens1 = ft_strlen(s1);
	lens2 = ft_strlen(s2);
	temp = malloc(lens1 + lens2 + 1);
	if (!temp)
		return (NULL);
	ft_memcpy(temp, s1, lens1);
	ft_memcpy(temp + lens1, s2, lens2);
	temp[lens1 + lens2] = '\0';
	return (temp);
}
