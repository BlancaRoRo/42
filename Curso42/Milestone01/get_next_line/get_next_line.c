/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: blromero <blromero@student.42.com>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/24 16:46:57 by blromero          #+#    #+#             */
/*   Updated: 2026/06/28 17:16:29 by blromero         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_extract_line(char	*stash, int buf)
{
	size_t	index;

	index = 0;
	while (stash[index] != '\n' && stash[index])
		index++;
	if (buf)
	{
		if (stash[index] == '\n')
			return (ft_substr(stash, 0, index + 1));
		return (ft_substr(stash, 0, index));
	}
	if (stash[index] == '\0')
		return (NULL);
	return (ft_substr(stash, index + 1, ft_strlen(stash)- (index - 1)));
}

char	*ft_read_join(int fd, char *stash)
{
	char	*buffer;
	int		bytes_leidos;
	char	*temp;

	bytes_leidos = 1;
	if (!stash)
		stash = ft_clean_alloc(1);
	buffer = malloc(sizeof(char) * BUFFER_SIZE + 1);
	if (!stash || !buffer)
		return (free(stash), free(buffer), NULL);
	while (!ft_strchr(stash, (int) '\n') && bytes_leidos != 0)
	{
		bytes_leidos = read(fd, buffer, BUFFER_SIZE);
		if (bytes_leidos == -1)
			return (free(buffer), free(stash), NULL);
		buffer[bytes_leidos] = '\0';
		temp = ft_strjoin(stash, buffer);
		free(stash);
		stash = temp;
	}
	free(buffer);
	return (stash);
}

char	*get_next_line(int fd)
{
	char		*buffer;
	static char	*stash;
	char		*temp;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (free(stash), NULL);
	stash = ft_read_join(fd, stash);
	if (!stash)
		return (NULL);
	if (stash[0] == '\0')
	{
		free(stash);
		stash = NULL;
		return (NULL);
	}
	buffer = ft_extract_line(stash, 1);
	temp = ft_extract_line(stash, 0);
	free(stash);
	stash = temp;
	return (buffer);
}
int main(void)
{
    int     fd;
    char    *line;

    fd = open("only_nl.txt", O_RDONLY);
    
    // Llamada 1: devuelve "\n"
    line = get_next_line(-2);
    free(line);

    close(fd);

    // Llamada 3: aquí peta -> debe devolver NULL sin segfault
    line = get_next_line(-1);
    free(line);

    close(fd);
    return 0;
}
