function bfs(graph, destination, n) {
    const distance = Array(n + 1).fill(-1);
    const queue = [destination];
    distance[destination] = 0;

    while (queue.length > 0) {
        const current = queue.shift();

        for (const next of graph[current]) {
            if (distance[next] === -1) {
                distance[next] = distance[current] + 1;
                queue.push(next);
            }
        }
    }

    return distance;
}

function solution(n, roads, sources, destination) {
    const graph = Array.from({ length: n + 1 }, () => []);
    roads.forEach(([v1, v2]) => {
        graph[v1].push(v2);
        graph[v2].push(v1);
    });

    const distance = bfs(graph, destination, n);
    return sources.map(source => distance[source]);
}