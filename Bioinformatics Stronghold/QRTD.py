import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(10000)

def solve():
    try:
        with open("input.INP", "r") as f1:
            content = f1.read().strip().splitlines()
    except FileNotFoundError:
        return

    lines = [line.strip() for line in content if line.strip()]
    if len(lines) < 3:
        return

    # 1. Parse Taxa
    taxa = lines[0].split()
    taxa_map = {name: i for i, name in enumerate(taxa)}
    n = len(taxa)
    
    # 2. Parse Trees into Adjacency Lists
    # We treat trees as unrooted for the quartet logic
    adj1, root1 = parse_newick_adj(lines[1], taxa_map, n)
    adj2, root2 = parse_newick_adj(lines[2], taxa_map, n)

    # 3. Calculate Size of Unresolved Sets |U(T1)| and |U(T2)|
    # A quartet is unresolved in T if the 4 taxa meet at a single node u and diverge into >=4 different subtrees.
    u1_count = count_unresolved_in_tree(adj1, n, root1)
    u2_count = count_unresolved_in_tree(adj2, n, root2)

    # 4. Calculate Size of Intersection |U(T1) intersect U(T2)|
    # We need to count quartets {a,b,c,d} that are unresolved in BOTH T1 and T2.
    # This happens if there is a node u in T1 and v in T2 such that a,b,c,d are in distinct branches of u AND v.
    intersect_count = count_common_unresolved(adj1, adj2, n, root1, root2)

    # 5. Formula: QD = |U1| + |U2| - 2*|Intersection|
    result = u1_count + u2_count - 2 * intersect_count

    with open("output.OUT", "w") as f2:
        f2.write(str(result))

def parse_newick_adj(newick, taxa_map, n):
    newick = newick.strip().replace(';', '')
    # Nodes 0 to n-1 are leaves. Internal nodes start at n.
    adj = {}
    for i in range(n):
        adj[i] = []
        
    stack = []
    curr = -1
    node_cnt = n - 1 # Start counting internal nodes from n
    
    # We'll use a standard parser but build an undirected graph
    # To handle the "unrooted" nature correctly later, we pick an arbitrary root for traversal (node n)
    
    # Create the first internal node (virtual root)
    node_cnt += 1
    root = node_cnt
    curr = root
    adj[curr] = []
    
    i = 0
    while i < len(newick):
        char = newick[i]
        if char == '(':
            node_cnt += 1
            new_node = node_cnt
            adj[new_node] = []
            adj[curr].append(new_node)
            adj[new_node].append(curr) # Undirected
            stack.append(curr)
            curr = new_node
            i += 1
        elif char == ',':
            curr = stack[-1]
            i += 1
        elif char == ')':
            curr = stack.pop()
            i += 1
        else:
            j = i
            while j < len(newick) and newick[j] not in "(),;":
                j += 1
            name = newick[i:j].strip()
            if name in taxa_map:
                leaf_idx = taxa_map[name]
                adj[curr].append(leaf_idx)
                adj[leaf_idx].append(curr)
            i = j
            
    # Collapse degree-2 nodes? For exact quartet distance, degree-2 nodes don't change topology
    # but might complicate "star" logic. The formula works if we treat edges as edges.
    # Unresolved quartets only occur at nodes with degree >= 4.
    return adj, root

def count_unresolved_in_tree(adj, n, root):
    """
    Counts quartets that form a 'star' topology at any node in the tree.
    For a node u with subtrees of sizes s1, s2, ..., sk, the number of unresolved quartets is
    the number of ways to pick 4 leaves, one from each of 4 distinct subtrees.
    This is the coefficient of x^4 in the polynomial Product(1 + s_i * x).
    """
    total_unresolved = 0
    
    # Get subtree sizes for every node relative to the "root"
    # To do this correctly for an unrooted tree, we must iterate every internal node,
    # treat it as the root, and get sizes of components connected to it.
    
    # Optimization: One global DFS to get subtree sizes relative to a fixed root.
    # Then for each node, the components are its children (sizes known) 
    # and its parent (size = N - sum(children)).
    
    parent_map = {}
    subtree_size = {}
    
    # Post-order traversal stack
    order = []
    stack = [root]
    visited = {root}
    parent_map[root] = None
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                parent_map[v] = u
                stack.append(v)
                
    # Calculate subtree sizes
    for u in reversed(order):
        sz = 1 if u < n else 0 # Leaves have size 1
        for v in adj[u]:
            if parent_map[v] == u:
                sz += subtree_size[v]
        subtree_size[u] = sz

    # Now calculate unresolved quartets at each internal node
    internal_nodes = [u for u in adj if u >= n]
    
    for u in internal_nodes:
        # Collect sizes of all branches attached to u
        sizes = []
        sum_sizes = 0
        for v in adj[u]:
            if parent_map[v] == u:
                s = subtree_size[v]
                sizes.append(s)
                sum_sizes += s
            else:
                # The "parent" direction branch
                s = n - subtree_size[u]
                sizes.append(s)
                sum_sizes += s
        
        # We need to choose 4 leaves from distinct branches.
        # This is elementary symmetric polynomial e4(sizes).
        # We can compute e4 in O(degree) using Newton sums or DP.
        # DP: ways[k] = ways to choose k leaves from distinct branches processed so far.
        
        # DP state: dp[x] = number of ways to pick x leaves from distinct previous branches
        dp = [0] * 5
        dp[0] = 1
        
        for s in sizes:
            # Iterate backwards to avoid using same branch twice
            for k in range(4, 0, -1):
                dp[k] = dp[k] + dp[k-1] * s
                
        total_unresolved += dp[4]
        
    return total_unresolved

def count_common_unresolved(adj1, adj2, n, root1, root2):
    """
    Counts quartets {a,b,c,d} unresolved in BOTH trees.
    This requires iterating pairs of nodes (u, v) from T1, T2.
    """
    # 1. Precompute leaf sets (as bitmasks or sorted lists) for every branch in T1
    # Actually, fast O(N^2) approach:
    # For every internal node u in T1, assign each leaf a 'color' based on which branch of u it is in.
    # Then for every internal node v in T2, check how leaves are distributed among its branches.
    
    # To speed up, we can store for each node u in T1: a map {leaf_id -> branch_id}
    # But generating this map is O(N^2) total. Acceptable for N=2000.
    
    # Better: Use leaf-to-node mapping.
    # T1_mapping[u][leaf] = branch_index
    
    # Let's perform the O(N^2) logic explicitly.
    
    internal_nodes1 = [u for u in adj1 if u >= n and len(adj1[u]) >= 4]
    internal_nodes2 = [v for v in adj2 if v >= n and len(adj2[v]) >= 4]
    
    if not internal_nodes1 or not internal_nodes2:
        return 0
        
    # Precompute Component Maps for T1
    # For each u in T1, leaf_component1[u] is a list/array where arr[leaf] = branch_id
    leaf_comp1 = {} 
    
    # Helper to build component map for a node
    def get_component_map(adj, u, total_n):
        comp_map = [-1] * total_n
        branch_idx = 0
        
        # We need to traverse outward from u to all leaves
        visited = {u}
        for neighbor in adj[u]:
            # BFS/DFS from neighbor
            q = [neighbor]
            visited.add(neighbor)
            while q:
                curr = q.pop()
                if curr < total_n:
                    comp_map[curr] = branch_idx
                for x in adj[curr]:
                    if x not in visited:
                        visited.add(x)
                        q.append(x)
            branch_idx += 1
        return comp_map, branch_idx

    # Build maps for T1 (only for relevant nodes)
    for u in internal_nodes1:
        leaf_comp1[u], _ = get_component_map(adj1, u, n)
        
    # Main Intersection Loop
    total_common = 0
    
    for v in internal_nodes2:
        # Get component map for v in T2
        v_map, v_branches = get_component_map(adj2, v, n)
        
        # We need to intersect v's partition with u's partition for all u in T1
        for u in internal_nodes1:
            u_map = leaf_comp1[u]
            
            # We want to count selection of 4 leaves such that:
            # u_map[leaf] are all distinct AND v_map[leaf] are all distinct.
            
            # Build contingency table: count[branch_u][branch_v]
            # Since we don't know number of branches in u easily, use dict
            counts = {} 
            
            for leaf in range(n):
                c_u = u_map[leaf]
                c_v = v_map[leaf]
                if (c_u, c_v) not in counts:
                    counts[(c_u, c_v)] = 0
                counts[(c_u, c_v)] += 1
            
            # Now we have a sparse matrix of counts.
            # We need to select 4 items from distinct rows AND distinct columns.
            # Use DP or Newton sums.
            # Since we just need distinct rows/cols, let's list the entries.
            entries = list(counts.items()) # [((r,c), count), ...]
            
            # DP state: dp[k][mask_cols] -> too slow?
            # Number of branches is typically small.
            # If branches are large (star graph), matrix is diagonal?
            
            # Efficient calculation for "4 distinct rows and columns":
            # This is equivalent to finding coefficient of x1*x2*x3*x4 * y1*y2*y3*y4...
            # A recursive backtracking search is fast enough because we only need depth 4
            # and the number of non-zero entries is N.
            
            total_common += count_4_distinct(entries)
            
    return total_common

def count_4_distinct(entries):
    """
    entries: list of ((row, col), count)
    Returns number of ways to pick 4 items with distinct rows and distinct cols.
    """
    # Filter small counts
    valid_entries = [e for e in entries if e[1] > 0]
    n_ent = len(valid_entries)
    if n_ent < 4:
        return 0
        
    ans = 0
    
    # We can use recursion with pruning
    # To avoid N^4, we restrict index ordering
    
    # Optimization: Use the fact that we pick 4. 
    # Iterate e1, e2, e3, e4 such that indices are increasing.
    
    # This is still potentially slow if dense. 
    # But usually tree partitions are correlated or sparse.
    # Let's try a simple recursive solver.
    
    memo = {}

    def solve_k(idx, k, used_rows, used_cols):
        state = (idx, k, used_rows, used_cols) # hashing sets is slow, use bitmask if possible
        # Since branch IDs are small integers (usually < degree), bitmask works.
        # But IDs are not normalized 0..degree.
        pass 

    # Iterative backtracking 
    # Stack stores: (entry_index, depth, current_product, used_rows_mask, used_cols_mask)
    # We need to map row/col IDs to 0..60 to use bitmasks effectively.
    
    rows = set(r for (r,c),_ in valid_entries)
    cols = set(c for (r,c),_ in valid_entries)
    
    # If not enough distinct rows or cols, return 0
    if len(rows) < 4 or len(cols) < 4:
        return 0

    # Sort entries to perhaps fail fast
    # Just iterate 4 loops?
    # O(E^4) where E is number of non-empty cells (at most N).
    # N=2000 -> N^4 is too big.
    # BUT, depth is only 4. 
    
    # Is there an O(E) or O(E^2) way?
    # Yes, using Elementary Symmetric Polynomials on matrices (Ryser's formula logic).
    # But for k=4, straight loop is:
    # Sum( count1 * count2 * count3 * count4 )
    # This is acceptable if 'entries' is small.
    # If star graph vs star graph, entries = N (diagonal). loop runs N times? No, 1 time (N choose 4).
    # If star vs unrelated star, entries = N*N? No, total entries always = N.
    # Ah! The sum of counts is N. The number of non-zero entries E is at most N.
    # So iterating 4 items is O(N^4) in worst case (e.g. 4 big clusters).
    # BUT we only sum if rows distinct and cols distinct.
    
    # We can optimize:
    # We need Sum( w_i w_j w_k w_l ) where r_i,r_j... distinct and c_i,c_j... distinct.
    # Let's use simple recursion.
    
    return rec_solve(valid_entries, 0, 4, set(), set())

def rec_solve(entries, idx, k, used_rows, used_cols):
    if k == 0:
        return 1
    if idx == len(entries):
        return 0
    
    # Skip
    res = rec_solve(entries, idx+1, k, used_rows, used_cols)
    
    # Take (if valid)
    r, c = entries[idx][0]
    count = entries[idx][1]
    
    if r not in used_rows and c not in used_cols:
        used_rows.add(r)
        used_cols.add(c)
        res += count * rec_solve(entries, idx+1, k-1, used_rows, used_cols)
        used_rows.remove(r)
        used_cols.remove(c)
        
    return res

if __name__ == "__main__":
    solve()