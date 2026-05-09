"""扑克游戏的完全小白版写法：只用列表和函数，不用类。"""

import random


# 4 种花色，按顺序编号为 0~3
SUITES = ['♠', '♥', '♣', '♦']

# 点数表：
# 下标 1~13 分别对应 A~K
FACES = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def make_card(suite_index, face):
    """创建一张牌。

    这里不用类，直接用一个列表保存牌的信息：
    [花色编号, 点数]
    例如 [0, 1] 表示 ♠A
    """
    return [suite_index, face]


def card_to_string(card):
    """把一张牌转换成可读字符串。"""
    suite_index = card[0]
    face = card[1]
    return SUITES[suite_index] + FACES[face]


def build_poker():
    """创建一副 52 张的牌。"""
    cards = []
    for suite_index in range(4):
        for face in range(1, 14):
            cards.append(make_card(suite_index, face))
    return cards


def shuffle_poker(cards):
    """洗牌。"""
    random.shuffle(cards)


def deal_one(cards, current_index):
    """发一张牌。

    返回两个值：
    1. 发出去的那张牌
    2. 新的发牌位置
    """
    card = cards[current_index]
    current_index += 1
    return card, current_index


def arrange_player_cards(player_cards):
    """整理手牌。

    排序规则：
    1. 点数优先
    2. 花色次之
    """
    player_cards.sort(key=lambda card: (card[1], card[0]))


def cards_to_string(cards):
    """把一组牌转换成字符串，方便打印。"""
    result = []
    for card in cards:
        result.append(card_to_string(card))
    return '[' + ', '.join(result) + ']'


def main():
    # 1. 创建一副牌
    poker = build_poker()

    # 2. 洗牌
    shuffle_poker(poker)

    # 3. 创建 4 个玩家
    # 每个玩家也不用类，直接用字典保存名字和手牌
    players = [
        {'name': '张三', 'cards': []},
        {'name': '李四', 'cards': []},
        {'name': '王五', 'cards': []},
        {'name': '麻子', 'cards': []},
    ]

    # current_index 表示当前发到第几张牌
    current_index = 0

    # 4. 轮流发牌，每人 13 张
    for _ in range(13):
        for player in players:
            card, current_index = deal_one(poker, current_index)
            player['cards'].append(card)

    # 5. 每个玩家整理手牌并输出
    for player in players:
        arrange_player_cards(player['cards'])
        print(f"{player['name']}: {cards_to_string(player['cards'])}")


if __name__ == '__main__':
    main()
