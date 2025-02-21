function animateNumbers(elements) {
    // Define o intervalo de tempo em milissegundos
    const interval = 20;

    // Define o número de iterações da animação
    const iterations = 100;

    // Itera sobre a lista de elementos HTML
    for (let i = 0; i < elements.length; i++) {
        // Obtém o elemento HTML e os números inicial e final correspondentes
        const element = elements[i];
        const startNumber = 0;
        const endNumber = parseInt(element.innerHTML);

        // Calcula a diferença entre os números inicial e final
        const difference = endNumber - startNumber;

        // Calcula o incremento a ser adicionado ao número a cada iteração
        const increment = difference / iterations;

        // Inicializa o contador com o número inicial
        let count = startNumber;

        // Define a função que será executada a cada intervalo de tempo
        const updateCount = () => {
            // Adiciona o incremento ao contador
            count += increment;

            // Arredonda o contador para evitar números quebrados
            count = Math.round(count);

            // Atualiza o valor do elemento HTML com o novo contador
            element.innerHTML = count;

            // Verifica se o contador atingiu o valor final
            if (count >= endNumber) {
                // Para a animação
                clearInterval(intervalId);

                // Atualiza o valor do elemento HTML com o número final
                element.innerHTML = endNumber;
            }
        };

        // Inicia a animação
        const intervalId = setInterval(updateCount, interval);
    }
}
// Uso
const elements = document.querySelectorAll('.numero');
animateNumbers(elements);