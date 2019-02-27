
% this rule dissalowws compositional errors
:- error(R,T), reason(R),T=-1..n.


pitch(10..10+noOctaves).
rest(0).


% here is everything that is literally possible.
playing(X) :- pitch(X).
playing(X) :- rest(X).

level(1..10).

% voice 1 is bass, 2 is above bass, 3 is above 2, etc.
voice(1..voices).


% Generate
voices{instruction(P,V,I) :
	playing(P),
	voice(V)
	 }voices :- I=0..n.



% most general errors reasons
reason(e_polyphonic_single_voice).
reason(e_zero_voice).


% most general error rules
error(e_polyphonic_single_voice,I) :- instruction(A,V,I), instruction(B,V,I), A!=B, I=0..n.
error(e_zero_voice,I) :- instruction(A,V,I), V == 0.




#show instruction/3.








