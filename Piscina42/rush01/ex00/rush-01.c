/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush-01.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42malaga.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/19 11:42:20 by blromero          #+#    #+#             */
/*   Updated: 2025/07/19 12:19:43 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
void	print_matrix(char *str)
{
	if(check(str) == 1)
	{	
		write(1,"Error\n", 6);
		break;
	}
	while (i < 16)
	{
		if()
	}

	int i;
	int j;

	i = 0;
	j = 0;

	while(i < 4)
	{
		while(j < 4)
		{
			if(j < 3)
			{
				write(1,1);
                                write(1," ",1);
			}else
				write(1,1);
		}
		write(1,"\n",1);
	}
}

int	check(char *str)
{
	int i = 0;
	while(*str)
	{
		if( str < '1' && str > '4')
			return (1);
		str++;
		i++:
	}
	if (i != 16) return (1);
	return (0);
}
int[][]	generar_matrix(char *str)
{

}
