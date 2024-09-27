let totalPedido = 0;

        function adicionarPedido() {
            const sabor = document.getElementById("sabor").value;
            const tamanho = document.getElementById("tamanho").value;

            if (!sabor || !tamanho) {
                alert("Por favor, selecione o sabor e o tamanho.");
                return;
            }

            let valorPedido = 0;

            if (sabor === "CP") {
                if (tamanho === "P") valorPedido = 9;
                else if (tamanho === "M") valorPedido = 14;
                else valorPedido = 18;
            } else if (sabor === "AC") {
                if (tamanho === "P") valorPedido = 11;
                else if (tamanho === "M") valorPedido = 16;
                else valorPedido = 20;
            }

            totalPedido += valorPedido;

            const pedido = `Pedido: ${tamanho} de ${sabor} - Valor: R$ ${valorPedido}`;
            document.getElementById("pedido").innerText += pedido + "\n";
            document.getElementById("total").innerText = `Total: R$ ${totalPedido},00`;
        }