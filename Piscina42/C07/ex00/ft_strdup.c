/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/31 13:01:24 by blromero          #+#    #+#             */
/*   Updated: 2025/07/31 13:14:07 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int     ft_length(char *src)
{
	int	size;
	size = 0;
	while (src[size])
		size++;
	return (size);
}

char	*ft_strdup(char *src)
{
	char *cp;
	int	i;

	i = 0;
	cp = malloc(sizeof(char) * (ft_length(src) + 1));
	if (!cp)
		return (NULL);
	while (src[i])
	{
		cp[i] = src[i];
		i++;
	}
	cp[i] = '\0';
	return (cp);
}
