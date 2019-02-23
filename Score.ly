\version "2.18.0"
#(set-default-paper-size "letter" 'landscape)
#(set-global-staff-size 19)

\header {
	dedication = \markup{\italic"For Jordan Walsh"}
	title = "My battery is low and it's getting dark"
	subsubtitle = \markup{\italic{"
%name
"}}
	subtitle = \markup{\italic{"Solo Percussion and Electronics"}}
	composer = \markup{\column{" " "Brian Ellis" " "}}
	arranger = " " 
	tagline = \markup{\column{" " "www.brianellissound.com"}}
}

\paper{
  indent = 0\cm
  left-margin = 2\cm
  right-margin = 1\cm
  top-margin = 1\cm
  bottom-margin = 1\cm
  max-systems-per-page = 4
  ragged-last-bottom = ##f

}

\score {
	\midi {}
	\layout {}

<<

	\new Staff \with {
  instrumentName = #"Right"
  shortInstrumentName = #"R"
} \absolute {
    \once \override Staff.TimeSignature #'stencil = ##f 
	\override Score.BarNumber.stencil = ##f
	\override Score.BarLine.stencil = ##f
	\time 1/1
  \override Staff.StaffSymbol.line-count = #5

	\clef "percussion"
	\numericTimeSignature
%part0


	\revert Score.BarLine.stencil
	\bar "|."}



	\new Staff \with {
  instrumentName = #"Left"
  shortInstrumentName = #"L"
} \absolute {
    \once \override Staff.TimeSignature #'stencil = ##f 
	\override Score.BarNumber.stencil = ##f
	\override Score.BarLine.stencil = ##f
	\time 1/1
  \override Staff.StaffSymbol.line-count = #5

	\clef "percussion"
	\numericTimeSignature

%part1

	\revert Score.BarLine.stencil
	\bar "|."}


>>
}