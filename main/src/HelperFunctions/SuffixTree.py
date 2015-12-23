class SuffixTree:
    def __init__(self, str):
        self.root = self.__build_suffix_tree(str)

    class Node:
        def __init__(self, start, substr):
            self.start = start
            self.substr = substr
            self.branches = {}

    def __insert_into_tree(self, subroot, suffix, start):
        prefix_len = len(subroot.substr)
        new_suffix = str(suffix[prefix_len:])
        if(len(subroot.branches) == 0):
            left_child = self.Node(subroot.start, "")
            right_child = self.Node(start, new_suffix)
            subroot.branches[""] = left_child
            subroot.branches[new_suffix] = right_child
        else:
            for (substr, node) in subroot.branches.items():
                if len(substr) > 0 and new_suffix.startswith(substr):
                    self.__insert_into_tree(node, new_suffix, start)
                    break
            else:
                new_child = self.Node(start, new_suffix)
                subroot.branches[new_suffix] = new_child

    def __build_suffix_tree(self, t_str):
        len_str = len(t_str)
        i = len_str - 1
        root = self.Node(len_str, "")
        while i >= 0:
            self.__insert_into_tree(root, str(t_str[i:]), i)
            i -= 1
        return root

    def display_all_suffix(self):
        self.__display_all_suffix(self.root, "")

    def __display_all_suffix(self, subroot, suffix_s_prefix, level = 0):
        if len(subroot.branches) == 0:
            if subroot.substr == "":
                level -= 1
            print(suffix_s_prefix, level)
            return
        for (substr, node) in subroot.branches.items():
            self.__display_all_suffix(node, suffix_s_prefix + substr, level + 1)

stree = SuffixTree("abcabb")
stree.display_all_suffix()