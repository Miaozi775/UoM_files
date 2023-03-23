package comp26120;

import java.util.LinkedList;
import java.util.List;

public class hashset implements set<String> {
    int verbose;
    HashingModes mode;

    speller_config config;

    cell[] cells;
    int size;
    int num_entries; // number of cells in_use

    // TODO add any other fields that you need
    int collisions = 0;
    List<String>[] linkCells;

    // This is a cell structure assuming Open Addressing
    // You wil need alternative data-structures for separate chaining
    public class cell { // hash-table entry
        String element; // only data is the key itself
        state state;
        public cell(String ele){
            element = ele;
        }
    }

    public static enum state {
        empty, in_use, deleted;
    }

    public hashset(speller_config config) {
        verbose = config.verbose;
        mode = HashingModes.getHashingMode(config.mode);

        // TODO: create initial hash table
        cells = new cell[13];
        size = 0;

        if(mode == HashingModes.HASH_1_SEPARATE_CHAINING || mode == HashingModes.HASH_2_SEPARATE_CHAINING){
            linkCells = new LinkedList[13];
        }
    }

    // Helper functions for finding prime numbers
    public boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++)
            if (n % i == 0)
                return false;
        return true;
    }

    public int nextPrime(int n) {
        int i = n;
        while (!isPrime(i)) {
            i++;
        }
        return i;
    }

    public void insert(String value) {
        if(size == cells.length){
            expand();
        }
        
        int index = hashcode(value);

        if(mode == HashingModes.HASH_1_SEPARATE_CHAINING || mode == HashingModes.HASH_2_SEPARATE_CHAINING){
            insertByLink(value, index);
            return;
        }

        while(index == -2){
            expand();
            index = hashcode(value);
        }

        // SeparateChaining will return -1 as result
        // if find value in the set will return -1
        if(index >= 0){
            if(cells[index] == null){
                cells[index] = new cell(value);
                size++;
            }else{
                return;
            }
        }
    }

    public boolean find(String value) {
        int index = hashcode(value);
        if(mode == HashingModes.HASH_1_SEPARATE_CHAINING || mode == HashingModes.HASH_2_SEPARATE_CHAINING){
            return findByLink(value, index);
        }

        if(index < 0){
            return false;
        }
        if(cells[index] == null){
            return false;
        }
        if(value.equals(cells[index].element)){
            return true;
        }
        return false;
    }

    public void print_set() {
        System.out.print("hashset:\n");
        for (int i = 0; i < cells.length; i++) {
            System.out.format("\t%s\n", cells[i] == null ? null : cells[i].element);
        }
    }

    public void print_stats() {
        System.out.format("hashset contains %d elements\n", size);
        System.out.format("average collision per access is %.2f\n", (collisions+0.0)/size);
    }

    // Hashing Modes

    public enum HashingModes {
        HASH_1_LINEAR_PROBING, // =0 in mode flag
        HASH_1_QUADRATIC_PROBING, // =1,
        HASH_1_DOUBLE_HASHING, // =2,
        HASH_1_SEPARATE_CHAINING, // =3,
        HASH_2_LINEAR_PROBING, // =4,
        HASH_2_QUADRATIC_PROBING, // =5,
        HASH_2_DOUBLE_HASHING, // =6,
        HASH_2_SEPARATE_CHAINING; // =7

        public static HashingModes getHashingMode(int i) {
            switch (i) {
            case 1:
                return HASH_1_QUADRATIC_PROBING;
            case 2:
                return HASH_1_DOUBLE_HASHING;
            case 3:
                return HASH_1_SEPARATE_CHAINING;
            case 4:
                return HASH_2_LINEAR_PROBING;
            case 5:
                return HASH_2_QUADRATIC_PROBING;
            case 6:
                return HASH_2_DOUBLE_HASHING;
            case 7:
                return HASH_2_SEPARATE_CHAINING;
            default:
                return HASH_1_LINEAR_PROBING;
            }
        }
    }

    // Your code

    
    private void insertByLink(String value, int index){
        if(linkCells[index] == null){
            LinkedList list = new LinkedList<>();
            list.add(value);
            linkCells[index] = list;
        }else{
            linkCells[index].add(value);
        }
    }

    private boolean findByLink(String value, int index){
        if(linkCells[index] == null){
            return false;
        }else{
            for(Object o : linkCells[index]){
                if(value.equals(o)){
                    return true;
                }
            }
            return false;
        }
    }

    private void expand(){
        if(mode == HashingModes.HASH_1_SEPARATE_CHAINING || mode == HashingModes.HASH_2_SEPARATE_CHAINING){
            expandByList();
            return;
        }
        int len2 = 2 * cells.length;
        int prime = nextPrime(len2);
        cell[] old = cells;
        cells = new cell[prime];
        int old_size = old.length;
        size = 0;
        for(int i=0;i<old_size;i++){
            if(old[i] != null){
                insert(old[i].element);
            }
        }
    }
    private void expandByList(){
        int len2 = 2 * linkCells.length;
        int prime = nextPrime(len2);
        List[] old = linkCells;
        linkCells = new LinkedList[prime];
        int old_size = old.length;
        size = 0;
        for(int i=0;i<old_size;i++){
            if(old[i] != null){
                for(Object o : old[i]){
                    insert(String.valueOf(o));
                }
            }
        }
    }

    private int hashcode(String value){
        switch (mode) {
            case HASH_1_QUADRATIC_PROBING:
                return hash1QuadraticProbing(value);
            case HASH_1_DOUBLE_HASHING:
                return hash1DoubleHashing(value);
                case HASH_1_SEPARATE_CHAINING:
                return hash1SeparateChaining(value);
                case  HASH_2_LINEAR_PROBING:
                return hash2LinearProbing(value);
                case HASH_2_QUADRATIC_PROBING:
                return hash2QuadraticProbing(value);
                case HASH_2_DOUBLE_HASHING:
                return hash2DoubleHashing(value);
                case HASH_2_SEPARATE_CHAINING:
                return hash2SeparateChaining(value);
            default:
                return hash1LinearProbing(value);
            }
    }

    private int hash1LinearProbing(String value){
        int index = hashfun1(value);
        int i = 0;
        while(i < cells.length){
            if(cells[index] == null){
                return index;
            }
            if(value.equals(cells[index].element)){
                return index;
            }
            collisions++;
            index = (index+1)%cells.length;
            i++;
        }
        return -1;
    }
    private int hash1QuadraticProbing(String value){
        int index = hashfun1(value);
        int i = 0;
        while(i < cells.length){
            if(cells[index] == null){
                return index;
            }
            if(value.equals(cells[index].element)){
                return index;
            }
            collisions++;
            index = (index+ i*i)%cells.length;
            i++;
        }
        return -2;
    }
    private int hash1DoubleHashing(String value){
        int index = hashfun1(value);
        int i = 0;
        while(i < cells.length){
            if(cells[index] == null){
                return index;
            }
            if(value.equals(cells[index].element)){
                return index;
            }
            collisions++;
            index = (index+ i*hashfun2(value))%cells.length;
            index = index > 0 ? index : -index;
            i++;
        }
        return -2;
    }
    private int hash1SeparateChaining(String value){
        int index = hashfun1(value);
        return index;
    }
    private int hash2LinearProbing(String value){
        int index = hashfun2(value);
        int i = 0;
        while(i < cells.length){
            if(cells[index] == null){
                return index;
            }
            if(value.equals(cells[index].element)){
                return index;
            }
            collisions++;
            index = (index+1)%cells.length;
            i++;
        }
        return -1;
    }
    private int hash2QuadraticProbing(String value){
        int index = hashfun2(value);
        int i = 0;
        while(i < cells.length){
            if(cells[index] == null){
                return index;
            }
            if(value.equals(cells[index].element)){
                return index;
            }
            collisions++;
            index = (index+ i*i)%cells.length;
            i++;
        }
        return -2;
    }
    private int hash2DoubleHashing(String value){
        int index = hashfun2(value);
        int i = 0;
        while(i < cells.length){
            if(cells[index] == null){
                return index;
            }
            if(value.equals(cells[index].element)){
                return index;
            }
            collisions++;
            index = (index+ i*hashfun1(value))%cells.length;
            index = index > 0 ? index : -index;
            i++;
        }
        return -2;
    }
    private int hash2SeparateChaining(String value){
        int index = hashfun2(value);
        return index;
    }

    private int hashfun1(String value){
        int code = 1;
        for(int i=0;i<value.length();i++){
            code = code * (int)value.charAt(i);
        }
        code = code % cells.length;
        if(code < 0){
            code = -code;
        }
        return code;
    }
    private int hashfun2(String value){
        int code = 1;
        for(int i=0;i<value.length();i++){
            code = code + (int)value.charAt(i);
        }
        code = code % cells.length;
        if(code < 0){
            code = -code;
        }
        return code;
    }
}
