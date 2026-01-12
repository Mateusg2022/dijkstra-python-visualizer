<h2>Dijkstra Visualizer</h2>

<p>O Dijkstra é um algoritmo de grafos usado para encontrar o menor caminho entre dois nós. Com a implementação usando fila de prioridade mínima, sua complexidade de tempo é O(E * log V), e a espacial é de O(V) (para manter a priority queue)</p>
<p>Este projeto tem como intuito apresentar uma implementação mínima do Dijkstra e mostrar o grafo resultante usando a biblioteca Networkx, ideal para trabalhar com grafos.</p>
<p>Para criar um grafo inicial, usa-se a função generalized_petersen_graph (cria dois grafos, um de polígono e outro estrela, e os conecta).</p>
<p>O peso das arestas é definido aleatoriamente usando random.randint(1,100).
<p>Além disso, por padrão deixei que o algoritmo procurasse caminho entre os vértices 0 e 4. Para mudar, basta alterar na chamada do dijkstra(0, 4).</p>

<img width="562" height="485" alt="image" src="https://github.com/user-attachments/assets/05947c37-cc4b-45d5-b14b-40d5f254836d" />

<h2>Setup:</h2>

Dentro de um ambiente virtual:

  - Instale a biblioteca Networkx: ```pip install networkx```

  - Instale a biblioteca Matplotlib: ```pip install matplotlib```
  
  - Rode o programa: ```python dijkstra.py```
