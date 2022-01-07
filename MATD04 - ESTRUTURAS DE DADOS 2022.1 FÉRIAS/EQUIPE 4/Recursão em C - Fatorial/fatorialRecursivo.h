int factRecursivo(int n) {

    int fat = 0;

	if (n == 0 || n == 1) //CASO BASE PARA NÃO ENTRAR EM LOOP INFINITO

		return 1; //RETORNA 1 PARA SER MULTIPLICADO QUANDO TERMINAR AS CHAMADAS DE FUNÇÃO

	else

    {
        fat = n * factRecursivo(n - 1); //CASO GERAL: n! = n × (n-1)!

    } return fat;

		
}