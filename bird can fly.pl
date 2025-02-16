% Database of birds and whether they can fly
can_fly(pigeon).
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).

% Predicate to check if a bird can fly
flies(Bird) :-
    can_fly(Bird).
flies(Bird) :-
    \+ cannot_fly(Bird).