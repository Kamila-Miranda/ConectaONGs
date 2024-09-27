// Aguarde até que o DOM esteja completamente carregado
    document.addEventListener("DOMContentLoaded", function() {
        // Se houver mensagens flash
        const flashMessages = document.querySelectorAll('.flash-message') // Mudamos para selecionar pela classe flash-message
        if (flashMessages.length > 0) {
            // Após 3 segundos (3000 ms), remova as mensagens
            setTimeout(() => {
                flashMessages.forEach(msg => {
                    msg.style.display = 'none';
                });
            }, 2200); // Tempo em milissegundos
        }
    });

