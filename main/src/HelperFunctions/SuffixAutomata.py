class SuffixA:
    __maxLen = 12
    __st = []
    __sz = 0
    __last = 0

    class State:
        length = 0
        link = -1

        def __init__(self):
            self.nextSt = {}

    def __init__(self):
        self.__sz += 1
        for n in range(0, self.__maxLen + 1):
            self.__st.append(self.State())

    def sa_extend(self, c):
        cur = self.__sz
        self.__sz += 1

        self.__st[cur].length = self.__st[self.__last].length + 1

        p = self.__last
        while p != -1 and self.__st[p].nextSt.get(c) == None:
            self.__st[p].nextSt[c] = cur
            p = self.__st[p].link
        if p == -1:
            self.__st[cur].link = 0
        else:
            q = self.__st[p].nextSt[c]
            if (self.__st[p].length + 1 == self.__st[q].length):
                self.__st[cur].link = q
            else:
                clone = self.__sz
                self.__sz += 1
                self.__st[clone].length = self.__st[q].length + 1
                self.__st[clone].nextSt = self.__st[q].nextSt
                self.__st[clone].link = self.__st[q].link
                while p != -1 and self.__st[p].nextSt[c] == q:
                    self.__st[p].nextSt[c] = clone
                    p = self.__st[p].link
                self.__st[q].link = self.__st[cur].link = clone
            self.__last = cur