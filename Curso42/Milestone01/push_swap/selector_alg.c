/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   selector_alg.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/03 13:10:05 by blromero          #+#    #+#             */
/*   Updated: 2026/07/05 12:58:09 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_strcmp(char *s1, char *s2)
{	
	int	i;

	i = 0;
	while (s1[i] && s2[i])
	{
		if (s1[i] != s2[i])
			return ((unsigned int)s1[i] - (unsigned int)s2[i]);
	}
	return ((unsigned int)s1[i] - (unsigned int)s2[i]);
}

int	is_algorithm(char *argv)
{
	if (!argv)
		return (-1);
	if (ft_strcmp(argv, "--simple", size) == 0)
		return(0);
	if (ft_strcmp(argv, "--medium", size) == 0)
		return (1);
	if (ft_strcmp(argv, "--complex", size) == 0)
		return (2);
	if (ft_strcmp(argv, "--adaptive", size) == 0)
		return (3);
	return (-1);
}
