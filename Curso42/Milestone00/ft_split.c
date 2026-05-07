/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 17:30:01 by blromero          #+#    #+#             */
/*   Updated: 2026/05/07 19:53:47 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static void	ft_free_total(char **t)
{
	size_t	i;

	i = 0;
	if (!t)
		return ;
	while (t[i])
	{
		free(t[i]);
		i++;
	}
	free(t);
}

static int	ft_word_len(char const *s, size_t start, char c)
{
	int	index;
	int	len;

	len = 0;
	index = 0;
	while (s[start + index] && s[start + index] != c)
	{
		index++;
		len++;
	}
	return (len);
}

static int	ft_count_words(char const *s, char c)
{
	size_t	index;
	int		words;

	words = 0;
	index = 0;
	if (!s)
		return (0);
	while (s[index])
	{
		if (s[index] != c && (s[index + 1] == c || s[index + 1] == '\0'))
			words++;
		index++;
	}
	return (words);
}

static char	**ft_fill(char **t, char const *s, char c)
{
	size_t	i;
	size_t	index;
	size_t	len;

	i = 0;
	index = 0;
	while (s[index])
	{
		while (s[index] && s[index] == c)
			index++;
		if (s[index])
		{
			len = ft_word_len(s, index, c);
			t[i] = ft_substr(s, index, len);
			if (!t[i])
				return (ft_free_total(t), NULL);
			index += len;
			i++;
		}
	}
	t[i] = NULL;
	return (t);
}

char	**ft_split(char	const *s, char c)
{
	char	**t;

	if (!s)
		return (NULL);
	t = (char **)malloc(sizeof(char *) * (ft_count_words(s, c) + 1));
	if (!t)
		return (NULL);
	return (ft_fill(t, s, c));
}
