/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42malaga.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/30 19:45:01 by blromero          #+#    #+#             */
/*   Updated: 2025/07/31 12:36:20 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' && s2[i] != '\0' && s1[i] == s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

void	swap(char **str1, char **str2)
{
	char	*aux;

	aux = *str1;
	*str1 = *str2;
	*str2 = aux;
}

void	ft_print(char **argv)
{
	int	i;
	int	j;

	i = 1;
	j = 0;
	while (argv[i])
	{
		while (argv[i][j])
		{
			write(1, &(argv[i][j]), 1);
			j++;
		}
		j = 0;
		write (1, "\n", 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	int	i;
	int	j;

	j = 0;
	i = 1;
	if (argc < 1)
		return (0);
	while (argv[i])
	{
		j = i + 1;
		while (argv[j])
		{
			if (ft_strcmp(argv[i], argv[j]) > 0)
				swap(&argv[i], &argv[j]);
			j++;
		}
		i++;
	}
	ft_print(argv);
	return (0);
}
