from time import sleep
import random
import gdata
import gdata.youtube
import gdata.youtube.service
import pygame
import pygame.font
import wrapline
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

#pygame shit
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 400
BG_COLOR = 150, 150, 80
FG_COLOR = 100, 10, 10
pygame.init()
screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()
allsprites = []

#youtube shit
yt = gdata.youtube.service.YouTubeService()
yt.ssl = False
api_key, client_id = open('api_key.txt').read().split('\n')
yt.developer_key = api_key
yt.client_id = client_id

def generate_comment():
    most_discussed = yt.GetMostDiscussedVideoFeed()
    for video in most_discussed.entry:
        if video and video.comments:
            url = video.comments.feed_link[0].href
            comments = yt.GetYouTubeVideoCommentFeed(uri=url)
            for comment in comments.entry:
                yield str(comment.content.text)
def get_random_color():
    col_range = xrange(0,255)
    return random.choice(col_range),random.choice(col_range),random.choice(col_range)
def main():
    font_renderer = pygame.font.Font(pygame.font.get_default_font(), 15)
    com_gen = generate_comment()
    clock.tick(30)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                    f = font_renderer.render(com_gen.next(), True, get_random_color())
                    screen.blit(f, pygame.mouse.get_pos())
        #allsprites.append(f)
        #
        #Draw Everything
        #allsprites.update()
        #screen.blit(background, (0, 0))
        #allsprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()

