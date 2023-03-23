CXX := g++-11
CXX_STANDARD := 17
BUILTIN_TIDY := 1

ifeq ($(BUILTIN_TIDY), 1) 
TIDY := ./clang/bin/clang-tidy
else
TIDY := clang-tidy
endif

BINARIES := test-suite

all: ${BINARIES}

library.o: library.cpp library.h
	${CXX} -O3 -std=c++${CXX_STANDARD} -c $< -o $@ -Wall -Wextra

test-suite.o: test-suite.cpp library.h catch.h
	${CXX} -std=c++${CXX_STANDARD} -c $< -o $@ -w

catch.o: catch.cpp catch.h
	${CXX} -std=c++${CXX_STANDARD} -c $< -o $@ -w

%.o: %.cpp %.h
	${CXX} -std=c++${CXX_STANDARD} -c $< -o $@

%.o: %.cpp
	${CXX} -std=c++${CXX_STANDARD} -c $< -o $@ 

test-suite: catch.o library.o test-suite.o
	${CXX} -std=c++${CXX_STANDARD} $^ -o $@ -Wall -Wextra

analyze:
	${CXX} -O3 -std=c++${CXX_STANDARD} -c library.cpp -Wall -Wextra -fanalyzer -Wanalyzer-too-complex -Wno-analyzer-possible-null-argument

guidelines:
ifeq ($(BUILTIN_TIDY), 1) 
	${TIDY} -checks=cppcoreguidelines-*,clang-analyzer-* library.cpp -- std=c++${CXX_STANDARD} -I/usr/include/c++/9/ -I/usr/include/x86_64-linux-gnu/c++/9/
else
	${TIDY} -checks=cppcoreguidelines-*,clang-analyzer-* library.cpp -- std=c++${CXX_STANDARD}
endif


test: test-suite
	./test-suite

clean:
	rm -rf *.o ${BINARIES} *~
