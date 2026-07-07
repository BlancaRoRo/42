/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 21:36:23 by blromero          #+#    #+#             */
/*   Updated: 2026/05/06 20:25:28 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	index;
	char			*p;
	size_t			len;

	index = 0;
	if (!s || !f)
		return (NULL);
	len = ft_strlen(s);
	p = malloc (sizeof(char) * (len + 1));
	if (!p)
		return (NULL);
	while (s[index] != '\0')
	{
		p[index] = f(index, s[index]);
		index++;
	}
	p[index] = '\0';
	return (p);
}
