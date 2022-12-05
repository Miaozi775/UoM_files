#rule of out
test-suite:test-suite.o library.o catch.o
	g++ -o test-suite test-suite.o library.o catch.o 
#rule of test-suite.o
test-suite.o:test-suite.cpp library.h catch.h
	g++ -c -o test-suite.o test-suite.cpp -Ilibrary -Icatch
#rule of library.o
library.o:library.cpp library.h
	g++ -c -o library.o library.cpp
#rule of catch.o
catch.o:catch.cpp catch.h
	g++ -c -o catch.o catch.cpp
#clean rule
clean:
	rm -f out test-suite.o catch.o library.o
