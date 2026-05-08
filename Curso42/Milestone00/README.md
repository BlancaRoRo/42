# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    README.md                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: blromero <blromero@student.42.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/08 18:57:13 by blromero          #+#    #+#              #
#    Updated: 2026/05/08 19:49:10 by blromero         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
*Este proyecto ha sido creado como parte del currículo de 42 por Blromero*

# **'Descripción'**
Este proyecto llamado ***Libft*** contiene diversas funciones propias de la Librería Estándar de C, pero con una creación personal, aunque con la misma funcionalidad.
Como objetivo principal, tiene profundizar en la comprensión, entendimiento y gestión tanto de diversos tipos de variables de C, cómo en la gestión de memoria, comportamiento de punteros y uso de listas enlazadas.

Contiene una gran variedad de funciones básicas en C y funciones extra sobre el uso de listas enlazadas.
Además para la compilación contiene un Makefile y una librería "libft.h" que agrupa todas las funciones realizadasen el proyecto para poder hacer uso entre ellas.

# **'Instrucciones'**

*Compilación y Ejecución*
Para la compilación de las funciones se utiliza un `Makefile` con las reglas estándar exigidas: `all`, `clean`, `fclean`, `re` y `bonus`.

Para la compilación de funciones básicas en C:
`make`

Para limpieza de estas funciones:
`make clean` o  `make fclean`

Para la compilación de funciones bonus o listas enlazadas:
`make bonus`

*Instalación*
Tan solo debes descargar o clonar este repositorio y compilarlo en tu entorno local.

## Recursos
*   **Manual de C (man):** Utilizado para entender el comportamiento real y los casos borde de las funciones originales.
*   **IA:** Usada como apoyo para la corrección de algoritmos, resolución de dudas específicas y estructura del `Makefile`.
*   **Francinette:** Utilizado como tester final para asegurar que cada método cumple con precisión todas las pruebas de evaluación.

## Librería Libft.h
* Se ha creado una librería que agrupa cada uno de los métodos creados, tanto básicos de C como listas enlazadas.
* A su vez en dicha librería existe la estructura de lista enlazada principal que se usa en los métodos.
* Se ha hecho uso de métodos como write o malloc y, por tanto, se ha includo en la librería las dependencias necesarias para su correcto funcionamiento.

