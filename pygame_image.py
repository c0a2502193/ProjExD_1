import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  # 練習1
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 練習8：背景画像の左右反転
    kk_img = pg.image.load("fig/3.png")  # 練習3：こうかとん画像の読み込み
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()  # 練習10-1：こうかとんRectの取得
    kk_rct.center = 300, 200  # 練習10-2：こうかとん初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        kk_rct.move_ip((-1, 0))  # 何も押していない時は背景と同じ速度で左へ移動
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, 1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((2, 0))  # 左に-1されているので、+2すると差し引き+1で右へ進む

        x = tmr%3200  # 練習5：背景画像移動用の変数／練習9：ループ
        screen.blit(bg_img, [-x, 0])  # 練習2
        screen.blit(bg_img2, [-x+1600, 0])  # 練習7
        screen.blit(bg_img, [-x+3200, 0])  # 練習9
        screen.blit(kk_img, kk_rct)  # 練習4：こうかとんSurfaceの描画
        pg.display.update()
        tmr += 1        
        clock.tick(200)  # 練習6：FPSの変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()