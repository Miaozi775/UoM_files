package comp26120;

public class bstree implements set<String> {
    int verbose;

    String value;
    bstree left;
    bstree right;

    speller_config config;

    // TODO add fields for statistics
    int comparisons;
    int find_comparisons;
    int find = 0;

    public bstree(speller_config config) {
        verbose = config.verbose;
        this.config = config;
    }

    public int size() {
        // This presumes that if value is not null then (possibly empty) left and right
        // trees exist.
        if (tree()) {
            return 1 + left.size() + right.size();
        }
        return 0;
    }
    public int height() {
        if (tree()) {
            return 1 + left.height() > right.height() ? left.height() : right.height();
        }
        return 0;
    }

    public int comparisons(int type){
        if (tree()) {
            return type == 0? comparisons:find_comparisons + left.comparisons(type) + right.comparisons(type);
        }
        return type == 0? comparisons:find_comparisons;
    }

    public void insert(String value) {
        comparisons++;
        if (tree()) {
            // TODO if tree is not NULL then insert into the correct sub-tree
            if(value.equals(this.value)){
                return;
            }else if(value.compareTo(this.value) < 0){
                left.insert(value);
            }else{
                right.insert(value);
            }
        } else {
            // TODO otherwise create a new node containing the value and two sub-trees.
            this.value = value;
            left = new bstree(config);
            right = new bstree(config);
        }
    }

    public boolean find(String value) {
        find_comparisons++;
        if (tree()) {
            // TODO complete the find function
            if(value.equals(this.value)){
                find++;
                return true;
            }else if(value.compareTo(this.value) < 0){
                return left.find(value);
            }else{
                return right.find(value);
            }
        }
        // if tree is NULL then it contains no values
        if(size() == 1){
            find++;
        }
        return false;
    }

    private boolean tree() {
        return (value != null);
    }

    // You can update this if you want
    public void print_set_recursive(int depth) {
        if (tree()) {
            for (int i = 0; i < depth; i++) {
                System.out.print(" ");
            }
            System.out.format("%s\n", value);
            left.print_set_recursive(depth + 1);
            right.print_set_recursive(depth + 1);
        }
    }

    // You can update this if you want
    public void print_set() {
        System.out.print("Tree:\n");
        print_set_recursive(0);
    }

    public void print_stats() {
        System.out.format("bstree contains %d elements\n", size());
        System.out.format("bstree height is %d \n", height());
        System.out.format("average comparisons per insert is %.2f\n", (comparisons(0) + 0.0)/size());
        System.out.format("average comparisons per find is %.2f\n", (comparisons(1) + 0.0)/find);
    }
}
