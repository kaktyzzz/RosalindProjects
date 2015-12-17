# string s;
# int n;
#
# struct node {
# 	int l, r, par, link;
# 	map<char,int> next;
#
# 	node (int l=0, int r=0, int par=-1)
# 		: l(l), r(r), par(par), link(-1) {}
# 	int len()  {  return r - l;  }
# 	int &get (char c) {
# 		if (!next.count(c))  next[c] = -1;
# 		return next[c];
# 	}
# };
# node t[MAXN];
# int sz;

class node:
    def __init__(self, l = 0, r = 0, par = -1):
        self.l = l
        self.r = r
        self.par = par
        self.next = dict()

    def length(self):
        return self.r - self.r

    def getnext(self, c):
        if self.next.get(c) != None:
            next[c] = -1
        return next[c]


t = []

class state:
    def __init__(self, v, pos):
        self.v = v
        self.pos = pos

ptr = state(0, 0)

def go(st, l, r):
    global t

    while l < r:
        if st.pos == len(t[st.v]):
            st = state(t[st.v].getnext(s[l]), 0)
            if st.v == -1:
                return st
        else:
            if s[t[st.v].l + st.pos] != s[l]:
                return state(-1, -1)
            if r - l < t[st.v].length() - st.pos:
                return state(st.v, st.pos + r - l)
            l += t[st.v].length() - st.pos
            st.pos = t[st.v].length()
    return st

def split(st):
    global sz
    global t
    global s

    if st.pos == t[st.v].length():
        return st.v
    if st.pos == 0:
        return t[st.v].par
    v = t[st.v]
    sz += 1
    id = sz
    t[id] = node(v.l, v.l+st.pos, v.par)
    t[v.par].getnext(s[v.l]) = id
    t[id].getnext(s[v.l+st.pos]) = st.v
    t[st.v].par = id
    t[st.v].l += st.pos
    return id

def get_link(v):
    global t

    if t[v].link != -1:
        return t[v].link
    if t[v].par == -1:
        return 0
    to = get_link(t[v].par)
    t[v].link = split(go(state(to, len(t[to])), t[v].l + (t[v].par == 0), t[v].r))
    return t[v].link

def tree_extend(pos):
    global ptr
    global sz
    global s

    while 1:
        nptr = go(ptr, pos, pos + 1)
        if nptr.v != -1:
            ptr = nptr
            return
        mid = split(ptr)
        sz += 1
        leaf = sz
        t[leaf] = node(pos, n, mid)
        t[mid].get(s[pos]) = leaf

        ptr.v = get_link(mid)
        ptr.pos = len(t[ptr.v])
        if mid == False:
            break;


s = "abcabc"

sz = 1;


for i in range(0, len(s)):
    tree_extend(i)