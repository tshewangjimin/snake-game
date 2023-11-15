import unittest
import pygame

class TestGame(unittest.TestCase):
   def setUp(self):
       pygame.init()
       self.screen = pygame.display.set_mode((800, 600))
       self.background = pygame.image.load("green grass.png")
       self.test_surface = pygame.Surface((100,200))
       self.test_surface.fill((128,0,128))
       self.x_pos = 200
       self.running = True

   def test_game_loop(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               self.running = False
       self.x_pos += 1
       self.screen.blit(self.test_surface, (self.x_pos, 250))
       pygame.display.update()
       self.assertTrue(self.running)

   def tearDown(self):
       pygame.quit()

if __name__ == '__main__':
   unittest.main()
