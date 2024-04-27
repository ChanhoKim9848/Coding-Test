class Solution(object):
    def distMoney(self, money, children):
        money-=children
        if money<0:return -1
        if money/7==children and money%7==0:return children
        if money/7==children-1 and money%7==3: return children-2
        return min(children-7, money/7)
# All kids, except the last one, got 7 dollars, and the last kid got exactly 3 dollars.
# Only children - 2 kids can get exactly 8 dollars, as we need to re-distribute dollars between last two kids.
# We have exactly children * 7 dollars.
# This is the only case when all children receive exactly 8 dollars.
# Otherwise, no more than children - 1 can get exactly 8 dollars (even if we have a lot of money)
# And no more than money / 7 kids can get exactly 8 dollars (if our money is limited).