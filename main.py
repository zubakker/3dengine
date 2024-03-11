import pygame
import time

from camera import Camera
from plane import Plane

screen = pygame.display.set_mode((600, 600))
resolution = [200, 200]
position = [-1, 0.5, 0.5]
rotation = [0,0]
map = [ Plane(([0, 0, 0], [0, 0, 1], [0, 1, 0]), (255, 0, 0)),
        Plane(([-0.1, 0, 0], [0.1, 0, 1], [0.1, 1, 0]), (0, 255, 0)),
        ]
cam = Camera(resolution, position, rotation, map)

pygame.event.set_grab(True)
playing = True
pygame.mouse.set_pos((300, 300))
while playing:
    # pygame.mouse.set_pos((300, 300))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playing = False
                pygame.quit()
                break
                
                '''
            if event.key == pygame.K_UP:
                cam.move((0.1, 0, 0))
            if event.key == pygame.K_DOWN:
                cam.move((-0.1, 0, 0))
            if event.key == pygame.K_LEFT:
                cam.move((0, 0.1, 0))
            if event.key == pygame.K_RIGHT:
                cam.move((0, -0.1, 0))

            if event.key == pygame.K_w:
                cam.rotate(0, 0.1)
            if event.key == pygame.K_s:
                cam.rotate(0, -0.1)
            if event.key == pygame.K_a:
                cam.rotate(0.1, 0)
            if event.key == pygame.K_d:
                cam.rotate(-0.1, 0)
                '''

        if event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            cam.rotate(0.01*dx, 0.01*dy)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cam.move((0.1, 0, 0))
    if keys[pygame.K_s]:
        cam.move((-0.1, 0, 0))
    if keys[pygame.K_a]:
        cam.move((0, 0.1, 0))
    if keys[pygame.K_d]:
        cam.move((0, -0.1, 0))

    bef = time.time()
    cam.render()
    screen.blit(cam.get_display(), (200,200))
    pygame.display.update()
    # time.sleep(10)
    print(time.time() - bef)
