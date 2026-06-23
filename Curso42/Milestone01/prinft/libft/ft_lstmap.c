/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/03 11:44:21 by blromero          #+#    #+#             */
/*   Updated: 2026/05/07 16:41:16 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list		*nueva_lista;
	t_list		*nuevo_nodo;
	void		*nuevo_contenido;

	nueva_lista = NULL;
	if (!lst || !f || !del)
		return (NULL);
	while (lst)
	{
		nuevo_contenido = f(lst->content);
		nuevo_nodo = ft_lstnew(nuevo_contenido);
		if (!nuevo_nodo)
		{
			del(nuevo_contenido);
			ft_lstclear(&nueva_lista, del);
			return (NULL);
		}
		ft_lstadd_back(&nueva_lista, nuevo_nodo);
		lst = lst->next;
	}
	return (nueva_lista);
}
