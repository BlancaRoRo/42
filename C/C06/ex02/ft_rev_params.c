/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42malaga.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/30 18:36:29 by blromero          #+#    #+#             */
/*   Updated: 2025/07/30 19:44:20 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	size;
	int	i;

	i = 0;
	if (argc < 1)
		return (0);
	size = argc -1;
	while (size > 0)
	{
		i = 0;
		while (argv[size][i])
		{
			write(1, &argv[size][i], 1);
			i++;
		}
		write(1, "\n", 1);
		size--;
	}
	return (0);
}
