import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WIDTH, HEIGHT = 800, 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the font for the score
FONT = pygame.font.SysFont(None, 50)

# Set the speed of the ball
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create the ball
ball = pygame.Rect(WIDTH/2-10, HEIGHT/2-10, 20, 20)

# Create the paddles
paddle_left = pygame.Rect(50, HEIGHT/2-70, 20, 140)
paddle_right = pygame.Rect(WIDTH-70, HEIGHT/2-70, 20, 140)

# Set the score
score_left = 0
score_right = 0

# Set the clock
clock = pygame.time.Clock()

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_left.y -= 5
    if keys[pygame.K_s]:
        paddle_left.y += 5
    if keys[pygame.K_UP]:
        paddle_right.y -= 5
    if keys[pygame.K_DOWN]:
        paddle_right.y += 5
    
    # Move the ball
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y
    
    # Bounce the ball off the top and bottom of the screen
    if ball.y <= 0 or ball.y >= HEIGHT - 20:
        BALL_SPEED_Y *= -1
    
    # Bounce the ball off the paddles
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        BALL_SPEED_X *= -1
    
    # Score if the ball goes off the screen
    if ball.x <= 0:
        score_right += 1
        ball.x = WIDTH/2-10
        ball.y = HEIGHT/2-10
        BALL_SPEED_X *= -1
    if ball.x >= WIDTH - 20:
        score_left += 1
        ball.x = WIDTH/2-10
        ball.y = HEIGHT/2-10
        BALL_SPEED_X *= -1
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the paddles and ball
    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.ellipse(screen, WHITE, ball)
    
    # Draw the score
    score_text = FONT.render(f"{score_left} - {score_right}", True, WHITE)
    screen.blit(score_text, (WIDTH/2-25, 10))
    
    # Update the screen
    pygame.display.update()
    
    # Set the frame rate
    clock.tick(60)
