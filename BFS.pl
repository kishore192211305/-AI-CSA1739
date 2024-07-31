% Define edges of the graph
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, h).
edge(f, i).

% bidirectional edges
connected(X, Y) :- edge(X, Y).
connected(X, Y) :- edge(Y, X).

% BFS algorithm
bfs(Start, Goal) :-
    bfs([[Start]], Goal, Path),
    reverse(Path, RevPath),
    write('Path: '), write(RevPath), nl.

bfs([[Goal|Path]|_], Goal, [Goal|Path]).

bfs([CurrentPath|OtherPaths], Goal, Path) :-
    extend_path(CurrentPath, NewPaths),
    append(OtherPaths, NewPaths, Paths),
    bfs(Paths, Goal, Path).

extend_path([Node|Path], NewPaths) :-
    findall([NewNode,Node|Path],
            (connected(Node, NewNode), 
             \+ member(NewNode, [Node|Path])),
            NewPaths).