#const n = 100.
#const oneOne = 1.
#const totalDuration = 700.

% this rule dissalowws compositional errors
:- error(R,T), reason(R),T=-1..n.


time(0..totalDuration).


% Generate
oneOne{timeMark(T,I) :
	time(T)
	 }oneOne :- I=0..n.




reason(e_multiple_in_one).
reason(e_not_increasing).

%% error(e_multiple_in_one,I) :-
%% 	timeMark(T1,I),
%% 	timeMark(T2,I),
%% 	T1 != T2,
%% 	I = 0..n.

error(e_not_increasing,I):-
	timeMark(T1,I),
	timeMark(T2,I+1),
	T1 >= T2 - 4,
	I = 0..n.

#show timeMark/2.








