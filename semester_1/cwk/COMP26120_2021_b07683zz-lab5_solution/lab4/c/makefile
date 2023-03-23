CFLAGS=-g -Wall -std=c99
LDFLAGS=
CC=gcc $(CFLAGS)
PQ_FLAG=NONE
IMP_FLAG=none

# set flags based on input command

ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*llist1.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=llist1
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*llist2.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=llist2
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*bad1.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=bad1
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*bad1.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=bad1
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*bad2.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=bad2
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*bad3.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=bad3
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*bad4.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=bad4
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*bad5.*//g'))
PQ_FLAG=LLIST
IMP_FLAG=bad5
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*avltree.*//g'))
PQ_FLAG=AVLTREE
IMP_FLAG=avltree
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*skiplist.*//g'))
PQ_FLAG=SKIPLIST
IMP_FLAG=skiplist
endif
ifeq (,$(shell echo $(MAKECMDGOALS) | sed 's/.*binaryheap.*//g'))
PQ_FLAG=BINARYHEAP
IMP_FLAG=binaryheap
endif

# For Part 1a, make tests_<imp> e.g. "make tests_llist1"

tests_%: phony
	$(CC) $(LDFLAGS) -D$(PQ_FLAG) tests.c $(IMP_FLAG).c global.c -o $@ 

# For Part1a, to run tests, make run_tests_<imp> e.g. "make run_tests_llst1"

run_tests_%:
	for number in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19; do\
	  ./tests_$(IMP_FLAG) $$number ; \
	done

# For Part 2, make "<app>_<imp>" e.g. "make sorting_binaryheap" 

sorting_%: phony
	$(CC) $(LDFLAGS) -D$(PQ_FLAG) apps/sorting.c $(IMP_FLAG).c global.c -o $@ 

concat_%: phony
	$(CC) $(LDFLAGS) -D$(PQ_FLAG) apps/concat_finder.c $(IMP_FLAG).c global.c -o $@ 

# For Part2, you can use, e.g., run_sorting_all to time the results of different compiled implementations
# and you can use, e.g., run_sorting_llist1 to see the results of running a particular implementation

# Note: you can edit the first line of data/sorting_data to change the difficulty. If you delete the very slow
# linked list implementations and increase this number you may get more obvious results about which data
# structure is best for this application. Similarly, the ct workload is more difficult than the ct2 one.
# You can, of course, develop your own workloads if you want!

run_sorting_all:
	@for f in $(wildcard sorting_*); do\
	  echo "$$f" ; \
	  { time ./$$f < ../data/sorting_data > /dev/null ; }  2>&1 | grep real | sed 's/real[[:space:]]*//' ; \
	done

run_sorting_%:
	./sorting_$(IMP_FLAG) < ../data/sorting_data

run_concat_all:
	@for f in $(wildcard concat_*); do\
          echo "$$f" ; \
          { time ./$$f < ../data/concat_data > /dev/null ; }  2>&1 | grep real | sed 's/real[[:space:]]*//' ; \
        done

run_concat_%:
	./concat_$(IMP_FLAG) < ../data/concat_data

# For tidying up
tidy:
	-rm *.o 

# This is a hack to use PHONY along with implicit targets
# Including a dependency on phony ensures that the target always
# gets recompiled
phony:
.PHONY: phony 

