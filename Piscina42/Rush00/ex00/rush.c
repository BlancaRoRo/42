/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/12 12:42:04 by blromero          #+#    #+#             */
/*   Updated: 2025/07/12 12:55:40 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void ft_putchar (char c);

void rush(int x, int y)
{
    int row;
    int col;

    if (x <= 0 || y <= 0)
        return;

    row = 0;
    while (row < y)
    {
        col = 0;
        while (col < x)
        {
            
            if ((row == 0 && (col == 0 || col == x - 1)) ||(row == y - 1 && ( col == 0 || col == x - 1)))
                ft_putchar('o');
            else if (row == 0 || row == y - 1)
                ft_putchar('-');
            else if (col == 0 || col == x - 1)
                ft_putchar('|');
            else
                ft_putchar(' ');
		
            col++;
        }
        ft_putchar('\n');
        row++;
    }
}

