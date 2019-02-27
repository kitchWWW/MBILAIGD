#const n = 40.
#const key = 0.
#const totalTime = 5.
#const oneOne = 1.
#const voices = 3.
#const noOctaves = 4.

change(V,I) :-
	instruction(A,V,I),
	instruction(B,V,I+1),
	A != B.

change(I) :-
	voice(V),
	change(V,I).

%% true if a single voice has done all possible pitches
exists(P,V) :-
	instruction(P,V,I),
	I = 0 ..n.

missing(P,V) :-
	playing(P),
	voice(V),
	not exists(P,V).

reason(e_too_much_change).
reason(e_too_little_change).
reason(e_change_same_voice).
reason(e_L_higher_than_R).
reason(e_too_far_apart).
reason(e_non_zero_change).
reason(e_too_little_playing).
reason(e_too_stagnate_playing).
reason(e_not_play_everything).
reason(e_everything_off).

error(e_too_much_change,I):-
	change(V1,I),
	change(V2,I),
	V1 != V2,
	I = 0..n.

error(e_too_little_change,I):-
	not change(I),
	I = 0..n-1.

error(e_change_same_voice,I):-
	change(V,I),
	change(V,I+1),
	I = 0..n.

error(e_L_higher_than_R,I):-
	instruction(L,1,I),
	instruction(R,2,I),
	pitch(L),
	pitch(R),
	L > R,
	I = 0..n.

error(e_too_far_apart,I) :-
	instruction(L,1,I),
	instruction(R,2,I),
	pitch(L),
	pitch(R),
	L +1 < R,
	I = 0..n.


error(e_non_zero_change,I):-
	instruction(P1,V,I),
	instruction(P2,V,I+1),
	V > 0,
	V < 3,
	P1 != P2,
	P1 != 0,
	P2 != 0,
	I = 0..n.

error(e_too_little_playing,I):-
	instruction(0,V,I),
	instruction(0,V,I+1),
	instruction(0,V,I+2),
	I = 0..n-2.

error(e_too_stagnate_playing,I) :-
	instruction(P,V,I),
	instruction(P,V,I+1),
	instruction(P,V,I+2),
	instruction(P,V,I+3),
	instruction(P,V,I+4),
	instruction(P,V,I+5),
	instruction(P,V,I+6),
	instruction(P,V,I+7),
	instruction(P,V,I+8),
	instruction(P,V,I+9),
	instruction(P,V,I+10),
	I = 0..n-10.


error(e_not_play_everything,n) :-
	missing(Z,V),
	V = 1..voices,
	Z = 10..10+noOctaves.

error(e_everything_off,I):-
	instruction(0,1,I),
	instruction(0,2,I),
	instruction(0,3,I),
	I = 0..n.



instruction(0,1,0).
instruction(0,2,0).








#show missing/2.

%% #show change/2.