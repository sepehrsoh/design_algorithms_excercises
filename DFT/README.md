###DFT Method

[DFT method](https://en.wikipedia.org/wiki/DFT_matrix) use for calculate furriers series 

here we explain all function duty


```sq_mat(n)``` : creating n*n matrix with 1 elements


```Vandermonde(a,b)``` : return b*b vondermonde matrix with power of a 


```comp(a)``` : # creat complex array from a list


```DFT(a)``` : DFT function giving an array which describes ratios of polynomials<br>
- in first step we detect is our series complex or not , if it contains complex numbers we translate it to complex numbers which our language knows<br>
- then we use vondermonde function for create a vondermonde matrix with roots
- at last return multiple of vondermonde matris with our giving array which return result of furriers series 