/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42malaga.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/31 14:08:03 by blromero          #+#    #+#             */
/*   Updated: 2025/07/31 14:34:03 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	size;
	int	i;

	i = 0;
	size = 0;
	if (min >= max)
	{
		range = NULL;
		return (0);
	}
	range = malloc()

	return size;

}
int	main(void)
{	
	int i = 0;
	int j = 0;
	int **arr = malloc(sizeof(int) * 4);
	if(!arr)
	{
		perror("malloc");
		return (1);
	}
	while (i < 4)
	{
		arr[i] = malloc(sizeof(int) * 3);
		if(!arr[i])
		{
			perror("malloc");
			return(1);
		}

	}
	i = 0;
	while(i < 4)
	{
		while(j < 3)
		{
			arr[i][j] = i;
		}
		j = 0;
		i++;
	}
	ft_ultimate_range( arr, )
	return (0);
}
