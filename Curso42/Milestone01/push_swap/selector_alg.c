/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   selector_alg.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/03 13:10:05 by blromero          #+#    #+#             */
/*   Updated: 2026/07/18 12:48:51 by blromero         ###   ########.fr       */
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
		i++;
	}
	return ((unsigned int)s1[i] - (unsigned int)s2[i]);
}

int	is_algorithm(char *argv)
{
	if (!argv)
		return (-1);
	if (ft_strcmp(argv, "--simple") == 0)
		return(1);
	if (ft_strcmp(argv, "--medium") == 0)
		return (2);
	if (ft_strcmp(argv, "--complex") == 0)
		return (3);
	if (ft_strcmp(argv, "--adaptive") == 0)
		return (4);
	if (ft_strcmp(argv, "--bench") == 0)
		return (5);
	return (-1);
}

int	parse_flags(int	argc, char **argv, int	*algorithm, t_stats *s, int *start)
{
	int	index;
	int	cat_method;
	int	flag;
	
	cat_method = 0;
	index = 1;
	s->bench = 0;
	while (index < argc && (flag = is_algorithm(argv[index]))!= -1)
	{
		if (flag == 5)
			s->bench += 1;
		if (flag < 5 && flag > 0)
		{
			*algorithm = flag;
			cat_method += 1;
		}
		index++;
	}
	if (s->bench > 1 || cat_method > 1)
		return (0);
	*start = index;
	return (1);
}
