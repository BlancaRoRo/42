/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_params.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42malaga.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/30 18:11:11 by blromero          #+#    #+#             */
/*   Updated: 2025/07/30 18:36:02 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	j;

	i = 1;
	j = 0;
	if (argc < 1)
		return (0);
	while (argv[i])
	{
		while (argv[i][j])
		{
			write(1, &argv[i][j], 1);
			j++;
		}
		j = 0;
		i++;
		write (1, "\n", 1);
	}
	return (0);
}
