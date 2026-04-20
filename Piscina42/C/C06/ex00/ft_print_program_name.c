/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_program_name.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42malaga.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/29 19:56:31 by blromero          #+#    #+#             */
/*   Updated: 2025/07/29 20:06:24 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;

	i = 0;
	if (argc == 0)
		return (0);
	while (argv[0][i])
	{
		write(1, &(argv[0][i]), 1);
		i++;
	}
	write(1, "\n", 1);
	return (0);
}
