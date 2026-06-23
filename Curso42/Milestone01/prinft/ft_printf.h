/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/20 11:30:43 by blromero          #+#    #+#             */
/*   Updated: 2026/06/22 15:42:44 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdarg.h>
#include <stdio.h>
#include <unistd.h>

void	ft_putbase(unsigned long long n, char *base);
int		selector(va_list ap, char format);
int		ft_printf(char const *format, ...);
int		ft_count_digit(unsigned long long n, int base_len);
int		ft_putint_print(int c);
int		ft_putstr_print(char *s);
int		ft_putvoid_print(void *p);
int		ft_putunsigned_print(unsigned int c);
int		ft_puthex_print(unsigned int c, char *base);
