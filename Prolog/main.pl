% 1. Hello, World! program
hello_world :- 
    write('Hello, World!'), nl,
    format('This is the "Hello, World!" program.~n').

% 2. Program to check if an element is a member of a list
member(X, [X|_]) :- 
    format('~w is a member of the list.~n', [X]).
member(X, [_|T]) :- 
    member(X, T).

% 3. Program to append two lists
append([], L, L) :- 
    format('The result of appending [] and ~w is ~w.~n', [L, L]).
append([H|T], L, [H|R]) :- 
    append(T, L, R),
    format('The result of appending [~w|~w] and ~w is [~w|~w].~n', [H, T, L, H, R]).

% 4. Program to reverse a list
reverse([], []) :- 
    format('The result of reversing [] is [].~n').
reverse([H|T], R) :- 
    reverse(T, RevT), append(RevT, [H], R),
    format('The result of reversing [~w|~w] is [~w|~w].~n', [H, T, R, RevT]).

% 5. Program to find the length of a list
length([], 0) :- 
    format('The length of [] is 0.~n').
length([_|T], Len) :- 
    length(T, Len1), Len is Len1 + 1,
    format('The length of [..|~w] is ~w.~n', [T, Len]).

% 6. Program to find the maximum of two numbers
max(X, Y, X) :- 
    X >= Y,
    format('~w is the maximum between ~w and ~w.~n', [X, X, Y]).
max(X, Y, Y) :- 
    Y > X,
    format('~w is the maximum between ~w and ~w.~n', [Y, X, Y]).

% 7. Program to find the factorial of a number
factorial(0, 1) :- 
    format('The factorial of 0 is 1.~n').
factorial(N, Fact) :- 
    N > 0, Prev is N - 1, factorial(Prev, PrevFact), Fact is N * PrevFact,
    format('The factorial of ~w is ~w.~n', [N, Fact]).

% 8. Program to find the nth Fibonacci number
fibonacci(0, 0) :- 
    format('The 0th Fibonacci number is 0.~n').
fibonacci(1, 1) :- 
    format('The 1st Fibonacci number is 1.~n').
fibonacci(N, Fib) :- 
    N > 1, Prev1 is N - 1, Prev2 is N - 2, fibonacci(Prev1, Fib1), fibonacci(Prev2, Fib2), Fib is Fib1 + Fib2,
    format('The ~wth Fibonacci number is ~w.~n', [N, Fib]).

% 9. Program to find the sum of a list of numbers
sum([], 0) :- 
    format('The sum of [] is 0.~n').
sum([H|T],sum([H|T], Sum) :-
sum(T, SubTotal), Sum is H + SubTotal,
format('The sum of [~w|~w] is ~w.~n', [H, T, Sum]).

% 10. Program to find the smallest element in a list
smallest([H|[]], H) :-
format('~w is the smallest element of the list.~n', [H]).
smallest([H|T], S) :-
smallest(T, ST), (H < ST -> S = H ; S = ST),
format('The smallest element of [~w|~w] is ~w.~n', [H, T, S]).

% Dummy lists for testing the programs
test_list1([1, 2, 3, 4, 5]).
test_list2([6, 7, 8, 9, 10]).
test_list3([3, 2, 1, 5, 4]).
test_list4([10, 20, 30, 40, 50]).
test_list5([2, 4, 6, 8, 10]).

% Test all the programs with the dummy lists
test :-
hello_world,
member(3, test_list1),
member(9, test_list2),
append(test_list1, test_list2, _),
reverse(test_list3, _),
length(test_list4, _),
max(10, 5, _),
factorial(5, _),
fibonacci(10, _),
sum(test_list5, _),
smallest(test_list5, _).