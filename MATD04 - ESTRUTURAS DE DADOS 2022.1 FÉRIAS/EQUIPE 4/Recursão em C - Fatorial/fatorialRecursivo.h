int factRecursivo(int x) {

    int fat = 0;

	if (x == 1) //CASO BASE PARA NÃO ENTRAR EM LOOP INFINITO

		return 1; //RETORNA 1 PARA SER MULTIPLICADO QUANDO TERMINAR AS CHAMADAS DE FUNÇÃO

	else

    {
        fat = x * factRecursivo(x - 1);

    } return fat;

		
}