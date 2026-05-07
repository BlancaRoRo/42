/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/21 20:00:28 by blromero          #+#    #+#             */
/*   Updated: 2026/05/06 18:48:00 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlen(const char *s)
{
	const char	*p;
	size_t		index;

	p = s;
	index = 0;
	while (*p != '\0')
	{
		index++;
		p++;
	}
	return (index);
}
