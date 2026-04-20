/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/12 13:37:37 by blromero          #+#    #+#             */
/*   Updated: 2025/07/12 13:42:25 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putchar(char c);

void	line(int width, char start, char middle, char end)
{
	int	i;

	if (width <= 0)
		return ;
	ft_putchar(start);
	i = 1;
	while (i < width - 1)
	{
		ft_putchar(middle);
		i++;
	}
	if (width > 1)
		ft_putchar(end);
	ft_putchar('\n');
}

void	rush(int x, int y)
{
	int	i;

	if (x <= 0 || y <= 0)
		return ;
	i = 1;
	while (i <= y)
	{
		if (i == 1)
			line(x, 'A', 'B', 'C');
		else if (i == y)
			line(x, 'A', 'B', 'C');
		else
			line(x, 'B', ' ', 'B');
		i++;
	}
}

