// Giles Reger, 2019

#include <stdbool.h> 

enum HashingModes { HASH_1_LINEAR_PROBING=0, 
                    HASH_1_QUADRATIC_PROBING=1, 
                    HASH_1_DOUBLE_HASHING=2, 
                    HASH_1_SEPARATE_CHAINING=3,
                    HASH_2_LINEAR_PROBING=4, 
                    HASH_2_QUADRATIC_PROBING=5, 
                    HASH_2_DOUBLE_HASHING=6, 
                    HASH_2_SEPARATE_CHAINING=7};

typedef char* Value_Type;
// Should be redefined if changing Value_Type
int compare(Value_Type,Value_Type);


// This is a cell struct assuming Open Addressing
// You will need alternative data-structurs for separate chaining
typedef struct
{ // hash-table entry
  Value_Type element; // only data is the key itself
  enum {empty, in_use, deleted} state;
} cell;


struct  hashset
{
  cell *cells; 
  int size; // cell cells [table_size];
  int num_entries; // number of cells in_use
  //TODO add anything else that you need
  int collision;
};

struct hashset* initialize_set (int size);     
void tidy (struct hashset*); 

int size(struct hashset*);

struct hashset* insert (Value_Type, struct hashset*);

bool find (Value_Type, struct hashset*);

// Helper functions
void print_set (struct hashset*);
void print_stats (struct hashset*);
