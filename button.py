import pygame.font

class Button:

    def __init__(self, ai_game, msg):

        self.screen =  ai_game.screen
        self.screen_rect = self.screen.get_rect()


        self.width, self.height = 200,50
        self.Button_color (110,10,10)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.sysFont(None,48)

        self.rect = pygame.rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(msg)


    def _prep_message(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color, self.Button_color )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        self.screen.fill(self.Button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
