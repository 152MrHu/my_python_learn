"""
多态案例战斗平台
"""
from torch.fft import hfft2


class HeroFighter:
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

class EnemyFighter:
    def power(self):
        return 70

def object_play(hero: HeroFighter , enemy: EnemyFighter):
    if hero.power() >= enemy.power():
        print("英雄获胜")
    else:
        print("敌人获胜")



if __name__ == '__main__':
    # 不用多态完成对战
    h1 = HeroFighter()
    e1 = EnemyFighter()
    if h1.power() >= e1.power():
        print("英雄获胜")
    else:
        print("敌人获胜")
    # 使用多态完成对战
    h2 = AdvHeroFighter()
    e2 = EnemyFighter()
    object_play(h2, e2)
    object_play(e2, h2)