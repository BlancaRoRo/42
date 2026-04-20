/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/31 13:14:52 by blromero          #+#    #+#             */
/*   Updated: 2025/07/31 13:24:57 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>

int	*ft_range(int	min, int max)
{
	int	*arr;
	int	i;

	i = 0;
	arr = malloc(sizeof(int) * (max - min));

	while (min < max)
	{
		arr[i] = min;
		min++;
		i++;
	}
	return (arr);
}
