/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/25 16:11:46 by blromero          #+#    #+#             */
/*   Updated: 2026/06/27 19:03:48 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	size_t	index;

	index = 0;
	while (s[index])
		index++;
	return (index);
}

char	*ft_clean_alloc(size_t size)
{
	char	*result;
	size_t	index;

	if (size <= 0)
		return (NULL);
	result = malloc(sizeof(char) * size);
	if (!result)
		return (NULL);
	index = 0;
	while (index < size)
	{
		result[index] = '\0';
		index++;
	}
	return (result);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*result;
	size_t	s_len;
	size_t	index;

	if (!s)
		return (NULL);
	index = 0;
	s_len = ft_strlen((const char *)s);
	if (start > s_len)
	{
		return (ft_clean_alloc(1));
	}
	if (s_len - start < len)
		len = s_len - start;
	result = malloc(sizeof(char) *(len + 1));
	if (!result)
		return (NULL);
	while (index < len)
	{
		result[index] = s[start + index];
		index++;
	}
	result[index] = '\0';
	return (result);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*result;
	size_t	len1;
	size_t	index;

	if (!s1 || !s2)
		return (NULL);
	len1 = ft_strlen(s1);
	result = malloc(ft_strlen(s2) + len1 + 1);
	if (!result)
		return (NULL);
	index = 0;
	while (index < len1)
	{
		result[index] = s1[index];
		index++;
	}
	index = 0;
	while (s2[index])
	{
		result[len1 + index] = s2[index];
		index ++;
	}
	result[len1 + index] = '\0';
	return (result);
}

char	*ft_strchr(const char *s, int c)
{
	if (!s)
		return (NULL);
	while (*s)
	{
		if (*s == c)
			return ((char *)s);
		s++;
	}
	if (c == '\0')
		return ((char *)s);
	return (NULL);
}
