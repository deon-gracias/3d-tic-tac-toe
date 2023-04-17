% N-Queens problem
% Solution is a list of positions (row, col) for each queen
% such that no two queens threaten each other.
% Returns a solution to the N-Queens problem for a board of size N.
nqueens(N, Solution) :-
    % Create a list of integers from 1 to N.
    length(Solution, N),
    numlist(1, N, Rows),

    % Define the constraints.
    % 1. All queens must be in different rows.
    all_different(Rows),

    % 2. All queens must be in different columns.
    % Use the Solution list to represent the columns.
    % The i-th element of the Solution list is the column of the queen in the i-th row.
    % Therefore, all elements of the Solution list must be different.
    % Note that this is already guaranteed by the all_different/1 constraint above.
    %all_different(Solution),

    % 3. No two queens must be on the same diagonal.
    % A diagonal can be defined by the difference between row and column.
    % The difference between two rows is the same as the difference between two columns
    % if and only if the queens are on the same diagonal.
    % So we can use the constraint all_different/1 on the differences between
    % the row and the column for each queen.
    diagonal_constraints(Rows, Solution),

    % Use labeling to find a solution.
    labeling([ffc], Solution).

% diagonal_constraints(+Rows, +Cols)
% Enforces the diagonal constraints.
% For each pair of queens (i, j) such that i < j, enforce the constraint that
% the absolute value of the difference between Rows[i] and Rows[j] is different
% from the absolute value of the difference between Cols[i] and Cols[j].
% This guarantees that no two queens are on the same diagonal.
diagonal_constraints([], []).
diagonal_constraints([R1|Rs], [C1|Cs]) :-
    diagonal_constraints(Rs, Cs, R1, C1, 1).

diagonal_constraints([], [], _, _, _).
diagonal_constraints([R2|Rs], [C2|Cs], R1, C1, Offset) :-
    AbsDiff #= abs(R1 - R2),
    AbsDiff #\= abs(C1 - C2),
    Offset1 #= Offset + 1,
    diagonal_constraints(Rs, Cs, R1, C1, Offset1),
    diagonal_constraints(Rs, Cs, R2, C2, Offset1).

