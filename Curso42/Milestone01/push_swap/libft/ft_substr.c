/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 15:42:07 by blromero          #+#    #+#             */
/*   Updated: 2026/04/22 16:11:43 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*temp;
	size_t	index;
	size_t	lens;

	if (!s)
		return (NULL);
	lens = ft_strlen(s);
	index = 0;
	if (start > lens)
		return (ft_strdup(""));
	if (len > lens - start)
		len = lens - start;
	temp = malloc(len + 1);
	if (!temp)
		return (NULL);
	while (len > index)
	{
		temp[index] = s[start + index];
		index++;
	}
	temp[index] = '\0';
	return (temp);
}
