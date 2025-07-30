#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
char *cup ;
char *cdown ;
char *rl ;
char *rr ;
char **matrix;

int ft_is_number(char c)
{
    return (c >='1' && c <='4');
}
int ft_correct(char **argv)
{
    int i;
    int bien;

    i = 0;
    bien = 0;
    while(argv[1][i])
    {
        if(i % 2 == 0)
            if(!ft_is_number(argv[1][i]))
            {
                return (0);
            }
            else
            {
                if (argv[1][i] != ' ')
                return (0);
            }
            i++;
    }
    return (i==32 && bien);    
}

char    *ft_split(char **argv, int s, int d)
{
    char *sol;
    int i ;

    sol = malloc(d - s + 2);
    i = 0;
    while(s <= d)
    {
        if(ft_is_number(argv[1][s]))
        {
            sol[i] = argv[1][s];
            i++;
        }
        s++;
    }
    sol[i] = '\0';
    return sol;

}
void    ft_print()
{
    int i;
    int j;

    i = 0;
    while (i < 4)
    {
        j = 0;
        while (j < 4)
        {
            write(1, &matrix[i][j], 1);
            if (j != 3)
                write(1, " ", 1);
            j++;
        }
        write(1, "\n", 1);
        i++;
    }
}

int ft_uniq(int row, int col, char val)
{
    int j;

    j = 0;

    while(j < 4)
        {
            if(matrix[row][j] == val && matrix [j][col] == val)
                return 1;
            j ++;
        }
        return 0;

}
int check_row(int row)
{
    char *line;
    int i ;
    int j ;

    i = 0;
    while(i <= row)
    {
        line[i] = matrix[row][i];
        i++;
    }
    if(rl[row] == ft_view(line) && rr[row] == ft_view_r(line))
        return 0;
    return 1;
}

int check_col(int col)
{
    char *line;
    int i ;

    i = 0;
    while(i <= col)
    {
        line[i] = matrix[i][col];
        i++;
    }
    if(cup[col] == ft_view(line) && cdown[col] == ft_view_r(line))
        return 0;
    return 1;
}
int ft_view(char *line)
{
    int max = line[3];
    int i ;
    int visible;

    visible = 1;
    i = 0;
    while(i< 4)
    {
        if(line[i] > max)
        {
            visible++;
            max = line[i];
        }
        i++;
    }
    return visible;
}
int ft_view_r(char *line)
{
     int max = line[3];
    int i ;
    int visible;

    visible = 1;
    i = 3;
    while(i>= 0)
    {
        if(line[i] > max)
        {
            visible++;
            max = line[i];
        }
       i--;
    }
    return visible;
}
char **ft_solv(int row, int col)
{
    int val;
    int n_row;
    int n_col;


    val = 1;
    if (col == 3 && row == 3) return matrix;
    if (col == 3)
        n_row = row + 1;
    if(col == 3)
        n_col = 0;
    else
        n_col = col +1;
    while (val <= 4)
    {
        if(ft_uniq(row, col,(val + '0'))){
             matrix[row][col] = (val + '0');

             if(col == 3 && !check_row(row)) continue;
             if(row == 3 && !check_col(col)) continue;
             if (solve(n_row, n_col) )
                return 1;
        }
        val++;
    }
    matrix[row][col] = 0;
    return 0;

}
void    ft_rush01(char **argv)
{
    int n;
    matrix = malloc(sizeof(char*)*4);

    n = 0;
    while(n < 4)
    {
        matrix[n] = malloc(sizeof(char)*4);
        n++;
    }
    *cup = ft_split(**argv,0,3);
    *cdown = ft_split(**argv,4,7);
    *rl = ft_split(**argv,8,11);
    *rr = ft_split(**argv, 12,15);

    solve(matrix, 0 , 0);
    ft_print(matrix);
     n = 0;
    while(n < 4)
    {
        free(matrix[n]);
        n++;
    }
    free(matrix);
}

int main(int argc, char **argv)
{
    if(argc != 2 ||ft_correct(argv) != 1)
    {
        write(1, "Error\n", 6);
        return (0);
    }
    ft_rush01(argv);

}

