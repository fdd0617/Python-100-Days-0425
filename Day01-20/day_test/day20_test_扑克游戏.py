### 例子1：扑克游戏。
#
# 这份代码演示了一个简单的“洗牌 -> 发牌 -> 玩家拿牌 -> 整理手牌 -> 输出”的过程。
# 主要有 4 个类：
# 1. Suite: 花色枚举，定义黑桃/红桃/梅花/方块
# 2. Card:  一张牌，包含花色和点数
# 3. Poker: 一副牌，负责创建 52 张牌、洗牌、发牌
# 4. Player:玩家，负责接牌、整理手牌

"""
Suite
  └─ 定义 4 种花色
     SPADE / HEART / CLUB / DIAMOND

Card
  └─ 表示 1 张牌
     属性：
     - suite: 花色
     - face: 点数
     方法：
     - __lt__()   规定两张牌怎么比较大小
     - __repr__() 规定打印时怎么显示

Poker
  └─ 表示 1 副牌
     属性：
     - cards: 52 张 Card 对象组成的列表
     - current: 当前发到第几张
     方法：
     - shuffle()  洗牌
     - deal()     发 1 张牌
     - has_next   是否还有牌可发

Player
  └─ 表示 1 个玩家
     属性：
     - name: 玩家名字
     - cards: 玩家手牌列表
     方法：
     - get_one()  拿 1 张牌
     - arrange()  给手牌排序

"""

from enum import Enum
import random

class Suite(Enum):
    """花色枚举"""
    # range(4) 会得到 0, 1, 2, 3
    # 因此四种花色会分别对应这 4 个整数
    # 后面显示花色符号和排序时都会用到这个值
    SPADE, HEART, CLUB, DIAMOND = range(4)

# for suite in Suite:
#     print(f"{suite}: {suite.value}")


class Card:
    """定义 牌类  suite 花色  face 牌点数"""
    def __init__(self,suite,face):
        # suite 表示花色，例如 Suite.SPADE
        # face 表示点数，1~13 分别对应 A~K
        self.suite = suite
        self.face = face

    def __lt__(self, other):
        # __lt__ 表示 less than，也就是定义 < 怎么比较
        # list.sort() 排序时，会反复调用这个方法比较两张牌的大小
        if not isinstance(other, Card):
            # 如果比较对象不是 Card，就交给 Python 的其他机制处理
            return NotImplemented
        # 这里的比较规则是：
        # 先比点数 face，再比花色 suite.value
        # 例如：
        # (3, 0) < (5, 1)  True  -> 3 比 5 小
        # (7, 0) < (7, 1)  True  -> 点数相同，再比较花色编号
        return (self.face, self.suite.value) < (other.face, other.suite.value)

    def __repr__(self):
        # __repr__ 决定对象被打印时显示成什么样子
        # 如果没有这个方法，打印牌对象时会看到一串内存地址，不直观
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # self.suite.value 用来取对应的花色符号
        # self.face 用来取对应的点数字符串
        # 例如：Suite.SPADE.value 是 0，faces[1] 是 'A'
        # 最终就会拼成 '♠A'
        return f"{suites[self.suite.value]}{faces[self.face]}"
    
# 测试类
# card1 = Card(Suite.SPADE,5)
# card2= Card(Suite.HEART,13)
# print(card1)
# print(card2)

class Poker:
    """扑克类"""

    def __init__(self):
        # 创建一副完整的 52 张扑克牌
        # 外层循环遍历 4 种花色，内层循环遍历 1~13 点
        # 每组合一次，就生成一张 Card 对象
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1,14)]
        # current 表示“下一次要发的是第几张牌”
        # 初始为 0，表示还没发过牌
        self.current = 0

    def shuffle(self):
        """洗牌"""
        # 洗牌时把发牌位置重置回 0
        # 这样可以保证重新从牌堆顶部开始发
        self.current = 0
        # random.shuffle 会直接把列表顺序打乱
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        # 取出当前这张牌
        card = self.cards[self.current]
        # 发出去之后，指针向后移动一位
        self.current += 1
        # 返回这张牌，让外部拿到
        return card
    
    @property
    def has_next(self):
        """判断还有没有牌可以发"""
        # current 小于总牌数，说明还有牌
        # current 等于 52 时，说明整副牌已经发完
        return self.current < len(self.cards)
    
# 测试Poker类
# poker = Poker()
# print(poker.cards)
# poker.shuffle()
# print(poker.cards)


class Player:
    """玩家"""
    
    def __init__(self,name):
        # 玩家名字
        self.name = name
        # cards 是一个列表，保存玩家拿到的所有牌
        self.cards = []

    
    def get_one(self,card):
        """摸牌"""
        # 把发到的这张牌加入玩家手牌
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌 排序"""
        # 对手牌原地排序
        # 排序规则由 Card.__lt__ 决定
        self.cards.sort()


# 主程序开始：
# 1. 创建一副牌
# 2. 洗牌
# 3. 创建 4 个玩家
# 4. 轮流发牌，每人 13 张
# 5. 每个玩家整理手牌并输出

poker = Poker()
poker.shuffle()
players = [Player('张三'),Player('李四'),Player('王五'),Player('麻子')]
# 将牌轮流发到每个玩家的手上，每人 13 张
# 外层循环控制“发 13 轮”
# 内层循环控制“每轮给 4 个玩家各发 1 张”

for _ in range(14):
    for player in players:
        # 先从牌堆发出一张牌，再交给当前玩家
        player.get_one(poker.deal())


# 玩家整理手上的牌，然后输出名字和手牌

for player in players:
    player.arrange()
    # end='' 表示先不要换行，这样名字和牌会显示在同一行
    print(f"{player.name}: ",end='')
    print(player.cards)
