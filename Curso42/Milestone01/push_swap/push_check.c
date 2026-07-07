/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_check.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/03 09:59:13 by blromero          #+#    #+#             */
/*   Updated: 2026/07/03 12:59:00 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	is_valid_number(char *s)
{
	int	size;
	int	index;

	index = 0;
	size = 0;
	if (!s)
		return (0);
	if (s[index] == '-' || s[index] == '+')
		index++;
	while (s[index])
	{
		if (!ft_isdigit(s[index]))
			return (0);
		index++;
		size++;
	}
	if (size > 10)
		return (0);
	return (1);
}

int	data_check(char **argv, int start)
{
	if (!argv)
		return (0);
	while (argv[start])
	{
		if (!is_valid_number(argv[start]))
			return (0);
		start++;
	}
	return (1);
}

t_stack	*fill_stack(char ** argv, int start)
{
	int 	nb;
	t_stack *a;
	t_stack *nuevo;
	t_stack *tmp;

	a = NULL;
	while (argv[start])
	{
		nuevo = (t_stack *)malloc(sizeof(t_stack));
		if (!nuevo)
			return (NULL);
		nuevo -> value = ft_atoi(argv[start]);
		if (a == NULL)
			a = nuevo;
		else
		{
			tmp = a;
			while (tmp -> next)
				tmp = tmp -> next;
			tmp -> next = nuevo; 
		}
		start++;
	}
	return (a);
}
int	has_duplicate(t_stack *a)
{
	t_stack *tmp;

	while (a)
	{
		tmp = a->next;
		while (tmp)
		{
			if (tmp->value == a->value)
				return (0);
			tmp = tmp->next;
		}
		a = a->next;
	}
	return (1);
}
