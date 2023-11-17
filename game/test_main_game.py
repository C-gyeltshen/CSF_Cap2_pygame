import unittest
from unittest.mock import patch, Mock
from main_game import Player, Obstacle
import pygame

class TestPlayer(unittest.TestCase):
    # Setting up the player for testing
    @patch('pygame.image.load')
    @patch('pygame.mixer.Sound')
    @patch('pygame.sprite.Sprite.__init__')
    def setUp(self, mock_sprite, mock_sound, mock_image):
        self.player = Player()
        self.player.rect = pygame.Rect(0, 0, 10, 10)

    # Testing if player jumps when the space key is pressed
    @patch('pygame.key.get_pressed')
    def test_player_input(self, mock_get_pressed):
        mock_get_pressed.return_value = {pygame.K_SPACE: True}
        self.player.rect.bottom = 300
        self.player.player_input()
        self.assertEqual(self.player.gravity, -20)

    # Testing how gravity affects the player's position
    def test_apply_gravity(self):
        self.player.gravity = 10
        self.player.rect.y = 100
        self.player.apply_gravity()
        self.assertEqual(self.player.gravity, 11)
        self.assertEqual(self.player.rect.y, 111)

    # Testing player animation when not on the ground
    def test_animation_state(self):
        self.player.rect.bottom = 299
        self.player.animation_state()
        self.assertEqual(self.player.image, self.player.player_jump)

    # Testing the overall player update
    def test_update(self):
        with patch.object(self.player, 'player_input') as mock_input, \
             patch.object(self.player, 'apply_gravity') as mock_gravity, \
             patch.object(self.player, 'animation_state') as mock_animation:
            self.player.update()
            mock_input.assert_called_once()
            mock_gravity.assert_called_once()
            mock_animation.assert_called_once()

class TestObstacle(unittest.TestCase):
    # Setting up the obstacle for testing
    @patch('pygame.image.load')
    @patch('pygame.sprite.Sprite.__init__')
    def setUp(self, mock_sprite, mock_image):
        self.obstacle = Obstacle('fly')

    # Testing how obstacle animation state changes
    def test_animation_state(self):
        self.obstacle.animation_state()
        self.assertEqual(self.obstacle.animation_index, 0.1)

    # Testing the overall obstacle update
    def test_update(self):
        with patch.object(self.obstacle, 'animation_state') as mock_animation, \
             patch.object(self.obstacle, 'destroy') as mock_destroy:
            self.obstacle.update()
            mock_animation.assert_called_once()
            mock_destroy.assert_called_once()

    # Testing if obstacle gets destroyed when off the screen
    def test_destroy(self):
        self.obstacle.rect.x = -101
        with patch.object(self.obstacle, 'kill') as mock_kill:
            self.obstacle.destroy()
            mock_kill.assert_called_once()

if __name__ == '__main__':
    unittest.main()
