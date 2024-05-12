import os
import unittest
import pygame
from Shooter import *


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.display.set_mode((1, 1))
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()
        
    def test_initial_score(self):
        score_manager = ScoreManager()
        self.assertEqual(score_manager.score, 0)

    def test_update_score(self):
        score_manager = ScoreManager()
        score_manager.update_score(50)
        self.assertEqual(score_manager.score, 50)

    def test_reset_score(self):
        score_manager = ScoreManager()
        score_manager.update_score(50)
        score_manager.reset_score()
        self.assertEqual(score_manager.score, 0)

    def test_read_score(self):
        score_manager = ScoreManager()
        score_manager.score = 100
        score_manager.write_score()
        self.assertEqual(score_manager.read_score(), 100)
        
    def test_bullet_initialization(self):
        bullet = Bullet(100, 200, 1)
        self.assertEqual(bullet.rect.center, (100, 200))
        self.assertEqual(bullet.direction, 1)
        
    def test_bullet_movement(self):
        bullet = Bullet(100, 200, 1)
        bullet.update()
        self.assertEqual(bullet.rect.centerx, 100 + bullet.speed)
        
    def test_grenade_initialization(self):
        grenade = Grenade(200, 300, 1)
        self.assertEqual(grenade.rect.center, (200, 300))
        self.assertEqual(grenade.direction, 1)
        self.assertEqual(grenade.timer, 100)
        self.assertEqual(grenade.vel_y, -11)
        
    def test_grenade_movement(self):
        grenade = Grenade(200, 300, 1)
        grenade.update()
        self.assertEqual(grenade.rect.centerx, 200 + grenade.direction * grenade.speed)
        self.assertAlmostEqual(grenade.rect.centery, 300 + grenade.vel_y, delta=0.5)
        
    def test_item_box_creation(self):
        ammo_box = ItemBox('Ammo', 100, 200)
        self.assertEqual(ammo_box.item_type, 'Ammo')
        self.assertEqual(ammo_box.rect.midtop, (100 + TILE_SIZE // 2, 200 + (TILE_SIZE - ammo_box.image.get_height())))
        
    def test_player_initialization(self): 
        player = Soldier('player', 100, 200, 1.65, 5, 20, 5)
        self.assertEqual(player.health, 100)
        self.assertEqual(player.max_health, 100)
        self.assertEqual(player.ammo, 20)
        self.assertEqual(player.grenades, 5)
        self.assertEqual(player.direction, 1)
        self.assertEqual(player.vel_y, 0)
        self.assertFalse(player.jump)
        self.assertTrue(player.alive)
        self.assertFalse(player.dead)
        
    def test_player_shoot(self):
        player = Soldier('player', 100, 200, 1.65, 5, 20, 5)
        initial_ammo = player.ammo
        player.shoot()
        self.assertEqual(player.ammo, initial_ammo - 1)
        
        
    def test_enemy_initialization(self):
        enemy = Soldier('enemy', 200, 300, 1.65, 2, 20, 0)
        self.assertEqual(enemy.health, 100)
        self.assertEqual(enemy.max_health, 100)
        self.assertEqual(enemy.ammo, 20)
        self.assertEqual(enemy.grenades, 0)
        self.assertEqual(enemy.direction, 1)
        self.assertEqual(enemy.vel_y, 0)
        self.assertFalse(enemy.jump)
        self.assertTrue(enemy.alive)
        self.assertFalse(enemy.dead)
        
    def test_enemy_shoot(self):
        enemy = Soldier('enemy', 200, 300, 1.65, 2, 20, 0)
        initial_ammo = enemy.ammo
        enemy.shoot()
        self.assertEqual(enemy.ammo, initial_ammo - 1)
                     
        
if __name__ == '__main__':
    unittest.main()
