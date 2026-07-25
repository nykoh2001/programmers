from enum import Enum
from collections import defaultdict

TABLE_MAX_IDX = 51
    

def solution(commands):
    print_results = []
    
    table = [[""] * TABLE_MAX_IDX for _ in range(TABLE_MAX_IDX)]
    merge_hierarchy = {}
    
    def _find(val: tuple) -> tuple:
        if val not in merge_hierarchy:
            return val
        
        return _find(merge_hierarchy[val])
    
    def _union(val1: tuple, val2: tuple) -> None:
        val1_root = _find(val1)
        val2_root = _find(val2)
        if val1_root == val2_root:
            return
        
        merge_hierarchy[val2_root] = val1_root
        
    def _update_all_value(
        value1: str, value2: str
    ) -> None:
        nonlocal table
        for row_idx in range(1, TABLE_MAX_IDX):
            for col_idx in range(1, TABLE_MAX_IDX):
                root_r, root_c = _find((row_idx, col_idx))
                if table[root_r][root_c] == value1:
                    table[root_r][root_c] = value2

    
    for command in commands:
        command_splits = command.split()
        command_type, command_args = command_splits[0], command_splits[1:]
        
        # for row in table[1:5]:
        #     print(row[1:5])
        # print(f"command_type, command_args: {command_type, command_args}")
        
        if command_type == "UPDATE":
            len_args = len(command_args)
            if len_args == 2:
                value1, value2 = command_args
                _update_all_value(value1, value2)
                continue
                
            # len_args == 3:
            r_str, c_str, value = command_args
            r, c = int(r_str), int(c_str)
            root_r, root_c = _find((r, c))
            table[root_r][root_c] = value
            continue
        
        if command_type == "MERGE":
            r1, c1, r2, c2 = list(map(int, command_args))
            root_1 = _find((r1, c1))
            root_2 = _find((r2, c2))
            
            if root_1 == root_2:
                continue
                
            _union((r1, c1), (r2, c2))
            if table[root_1[0]][root_1[1]]:
                continue
            if table[root_2[0]][root_2[1]]:
                table[root_1[0]][root_1[1]] = table[root_2[0]][root_2[1]]
            

        if command_type == "UNMERGE":
            r, c = list(map(int, command_args))
            root = _find((r, c))
            root_value = table[root[0]][root[1]]
            
            child_to_remove = []
            for child in merge_hierarchy:
                top_parent = _find(child)
                if root == top_parent:
                    child_to_remove.append(child)
                    table[child[0]][child[1]] = ""
                    table[top_parent[0]][top_parent[1]] = ""
            
            for child_r, child_c in child_to_remove:
                merge_hierarchy.pop((child_r, child_c))
    
            if root_value:
                table[r][c] = root_value
            continue
        
        if command_type == "PRINT":
            r, c = list(map(int, command_args))
            root_r, root_c = _find((r, c))
            print_results.append(table[root_r][root_c] if table[root_r][root_c] else "EMPTY")
            continue
    
    return print_results
    