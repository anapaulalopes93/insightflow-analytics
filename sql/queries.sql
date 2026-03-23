SELECT SUM(Valor_Total) AS faturamento_total FROM vendas;

SELECT Categoria_Produto, SUM(Valor_Total) AS total_vendas FROM vendas GROUP BY Categoria_Produto ORDER BY total DESC;

SELECT Nome_Produto, SUM(Quantidade) AS total_vendido FROM vendas GROUP BY Nome_Produto ORDER BY total_vendido DESC;

SELECT ID_Cliente, AVG(Valor_Total) AS ticket_medio FROM vendas GROUP BY ID_Cliente ORDER BY ticket_medio DESC;

SELECT Nome_Produto, SUM(Quantidade) AS total_vendido, RANK() OVER (ORDER BY SUM(Quantidade) DESC) AS ranking FROM vendas GROUP BY Nome_Produto;