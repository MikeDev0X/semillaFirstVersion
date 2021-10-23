import pygame
from config import * #importas todo de la clase 
import math
import random

#lista de down images 
for i in range(1,4):
	name = "assets_test/MainCharacter/DOWN"+str(i)+".png"
	DOWNImages.append(pygame.image.load(name))
#lista left images
	name = "assets_test/MainCharacter/LEFT"+str(i)+".png"
	LEFTImages.append(pygame.image.load(name))

	name = "assets_test/MainCharacter/RIGHT"+str(i)+".png"
	RIGHTImages.append(pygame.image.load(name))
#lista up images	
	name = "assets_test/MainCharacter/UP"+str(i)+".png"
	UPImages.append(pygame.image.load(name))
#lista RUP images
	name = "assets_test/MainCharacter/RUP"+str(i)+".png"
	RUPImages.append(pygame.image.load(name))
#lista RDOWN images
	name = "assets_test/MainCharacter/RDOWN"+str(i)+".png"
	RDOWNImages.append(pygame.image.load(name))
#lista LUP images
	name = "assets_test/MainCharacter/LUP"+str(i)+".png"
	LUPImages.append(pygame.image.load(name))
#lista LDOWN images
	name = "assets_test/MainCharacter/LDOWN"+str(i)+".png"
	LDOWNImages.append(pygame.image.load(name))
#=========================================================
#=========================================================
	name = "assets_test/Enemy/L"+str(i)+"E.png"
	LEFTenemy.append(pygame.image.load(name))
#lista LEFT images 
	name = "assets_test/Enemy/R"+str(i)+"E.png"
	RIGHTenemy.append(pygame.image.load(name))
#lista RIGHT images
###MAPAS

for t in range(2):
	name = "assets_test/MainCharacter/RPUNCH"+str(t+1)+".png"
	name2 = "assets_test/MainCharacter/LPUNCH"+str(t+1)+".png"
	RPUNCHImages.append(pygame.image.load(name))
	LPUNCHImages.append(pygame.image.load(name2))


class Health_Bar():
	def __init__(self):
		self.current_health = 200
		self.max_health = 1000
		self.h_bar = 400
		self.h_ratio = self.max_health/ self.h_bar
		self.target_hp = 500
		self.speed = 7
		self.alive = True

	def receive_dmg(self, dmg):
		if self.target_hp > 0:
			self.target_hp -= dmg
		if self.target_hp <= 0:
			self.target_hp = 0
			self.alive = False

	def heal(self, hp):
		if self.target_hp < self.max_health:
			self.target_hp += hp
		if self.target_hp >= self.max_health:
			self.target_hp = self.max_health

	def update_health(self):
		transition_w = 0
		transition_c = (128, 0, 32)

		if self.current_health > self.target_hp:
			self.current_health -= self.speed
			transition_w = int((self.target_hp - self.current_health)/ self.h_ratio)
			transition_c = (46, 113, 42)

		if self.current_health < self.target_hp:
			self.current_health += self.speed
			transition_w = int((self.target_hp - self.current_health)/ self.h_ratio)
			transition_c = (128, 0, 32)

		health_bar_width = int(self.current_health / self.h_ratio)
		health_bar = pygame.Rect(10,45,health_bar_width,25)
		transition_bar = pygame.Rect(health_bar.right,45,transition_w,25)

		#pygame.draw.rect(screen,(255, 213, 0),health_bar)
		#pygame.draw.rect(screen,transition_c,transition_bar)	
		#pygame.draw.rect(screen,(255,255,255),(10,45,self.h_bar,25),4)
		#tenemos que ver de donde sacamos screen

	def isAlive(self):
		return self.alive

	def setAlive(self):
		if self.alive == False:
			self.alive = True


class Player(pygame.sprite.Sprite):
	def __init__(self,game,x,y):

		self.game = game
		self._layer = PLAYER_LAYER
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
    
		self.x = x * PLAYERPIXEL
		self.y = y * PLAYERPIXEL
		self.width = PLAYERPIXEL
		self.height = PLAYERPIXEL

		self.health = 100
		self.standing = True
		self.punchL = False
		self.punchR = False
	
		self.hitbox = (self.x, self.y, PLAYER_HITBOX[0],PLAYER_HITBOX[1])
		self.punchboxLeft = (self.x - 7, self.y+27,PLAYER_PUNCHBOX[0],PLAYER_PUNCHBOX[1])
		self.punchboxRight = (self.x + 41, self.y+27,PLAYER_PUNCHBOX[0],PLAYER_PUNCHBOX[1])

    #self.hitbox = (self.x + 70, self.y+11)
#estas son variables temporales que almacenan el cambio de movimientos dentro del ciclo
		self.x_change = 0
		self.y_change = 0

		self.facing = 'down'
		self.animation_loop = 1
		self.animation_loop_2 = 0
		 #posicion predeterminada de nuestro personaje
		
		image_to_load = pygame.image.load('assets_test/MainCharacter/DOWN1.png').convert()

		self.image = pygame.Surface([self.width, self.height]) 
		self.image.set_colorkey(WHITE)
		image = pygame.transform.scale(image_to_load, DEFAULT_IMAGE_SIZE)
		# creamos un rectangulo como la imagen de nuestro jugador
		
		self.image.blit(image, (0,0))
		#what it looks like

    

		self.rect = self.image.get_rect()# donde esta posisionado / hitbox / se hace del mismo tamaño que la imagen anteriormente definida
		self.rect.x = self.x
		self.rect.y = self.y
		#funcion actualizar movimiento

		self.alive = True
		self.hp = Health_Bar()
		
	def update(self):
		self.movement()
		self.animation()
		self.punch()
		self.rect.x += self.x_change
		self.rect.y += self.y_change
		#funcion de movimiento de personaje
		self.x_change = 0
		self.y_change = 0
		#if self.alive:
			#self.hp.update_health()	
			#self.alive = self.isAlive()
		#else:
			#pass
			#estas morido
    			
		
	def movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] and keys[pygame.K_d]:
				self.standing = False
				self.facing = 'rup'
				self.y_change -= PLAYER_SPEED
				self.x_change += PLAYER_SPEED
		elif keys[pygame.K_s] and keys[pygame.K_d]:
				self.standing = False
				self.facing = 'rdown'
				self.y_change += PLAYER_SPEED
				self.x_change += PLAYER_SPEED
		elif keys[pygame.K_w] and keys[pygame.K_a]:
				self.standing = False
				self.facing = 'lup'
				self.y_change -= PLAYER_SPEED
				self.x_change -= PLAYER_SPEED
		elif keys[pygame.K_s] and keys[pygame.K_a]:
				self.standing = False
				self.facing = 'ldown'	
				self.y_change += PLAYER_SPEED
				self.x_change -= PLAYER_SPEED
		elif keys[pygame.K_a]:
				self.facing = 'left'
				self.standing = False
				self.x_change -= PLAYER_SPEED
		elif keys[pygame.K_d]:
				self.facing = 'right'
				self.standing = False
				self.x_change += PLAYER_SPEED
		elif keys[pygame.K_w]:
				self.facing = 'up'
				self.standing = False
				self.y_change -= PLAYER_SPEED
		elif keys[pygame.K_s]:
				self.facing = 'down'
				self.standing = False
				self.y_change += PLAYER_SPEED
		elif keys[pygame.K_SPACE]:
			if self.facing == 'rup' or self.facing == 'rdown' or self.facing == 'right' or self.facing == 'up' or self.facing == 'down':
				self.facing = 'right'
				self.standing = False
				self.punchL = False
				self.punchR = True
			else:
				self.facing = 'left'
				self.standing = False
				self.punchL = True
				self.punchR = False
		else:
			self.standing = True
			self.punchL = False
			self.punchR = False
		self.hitbox = pygame.Rect(self.rect.x, self.rect.y, PLAYER_HITBOX[0],PLAYER_HITBOX[1])
		self.punchboxLeft = pygame.Rect(self.rect.x - 7, self.rect.y+27,PLAYER_PUNCHBOX[0],PLAYER_PUNCHBOX[1])
		self.punchboxRight = pygame.Rect(self.rect.x + 41, self.rect.y+27,PLAYER_PUNCHBOX[0],PLAYER_PUNCHBOX[1])


	def animation(self): #--------------------------------------------------------------------------------funcion donde dibujamos a nuestro personaje

		if self.facing == "down":
			if self.standing:
				self.image  = DOWNImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = DOWNImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1
		#========================fin
		elif self.facing == "up":
			if self.standing:
				self.image  = UPImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = UPImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1
		#=========================fin
		elif self.facing == "left":
			if self.punchL:
				self.image = LPUNCHImages[math.floor(self.animation_loop_2)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop_2 += 0.1
				if self.animation_loop_2 >= 2:
					self.animation_loop_2 = 0
			elif self.standing:
				self.image = LEFTImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = LEFTImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1
		#=========================fin
		elif self.facing == "right":
			if self.punchR:
				self.image = RPUNCHImages[math.floor(self.animation_loop_2)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop_2 += 0.1
				if self.animation_loop_2 >= 2:
					self.animation_loop_2 = 0
			elif self.standing:
				self.image = RIGHTImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = RIGHTImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1
		#==========================fin
		elif self.facing == "rup":
			if self.standing:
				self.image  = RUPImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = RUPImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1
		#========================fin
		elif self.facing == "rdown":
			if self.standing:
				self.image  = RDOWNImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = RDOWNImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1
		#=========================fin
		elif self.facing == "lup":
			if self.standing:
				self.image = LUPImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = LUPImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1
		#=========================fin
		elif self.facing == "ldown":
			if self.standing:
				self.image = LDOWNImages[0]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
			else:
				self.image = LDOWNImages[math.floor(self.animation_loop)]
				self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 1

	def punch(self):
		hitsR = pygame.Rect.colliderect(self.punchboxRight,self.game.cazador)
		hitsL = pygame.Rect.colliderect(self.punchboxLeft,self.game.cazador)

		if hitsR and self.punchR:
			print('PUNCH R!!')
		elif hitsL and self.punchL:
			print('PUNCH L!!')

	def draw_hitbox(self):
		self._layer = ENEMY_LAYER
		SC = self.game.screen
		pygame.draw.rect(surface=SC,color=BlACK, rect=self.punchboxRight,border_radius = 2)
		pygame.draw.rect(surface=SC,color=BlACK, rect=self.punchboxLeft,border_radius = 2)

		pygame.display.flip()		

class Block(pygame.sprite.Sprite):
	def __init__(self,game,x,y):
		self.game = game
		self._layer = BLOCK_LAYER
		self.groups = self.game.all_sprites, self.game.blocks
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x * TPIXEL
		self.y = y * TPIXEL
		self.width = TPIXEL
		self.height = TPIXEL
		#todo objeto en la pantalla necesita una imagen

		self.image = pygame.Surface([self.width, self.height])
		#todo objeto en la pantallla se pinta de azul
		self.image.fill(BLUE)
 		#se contornea maás chil de gobierno
		self.rect = self.image.get_rect()
		self.rect.y = self.y
		self.rect.x = self.x


class BackGround(pygame.sprite.Sprite):
	def __init__ (self,game,x,y):
		self.game = game
		self._layer = GROUND_LAYER
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.x = x * TPIXEL
		self.y = y * TPIXEL
		self.width = TPIXEL
		self.height = TPIXEL
		#self.image = pygame.Surface([self.width, self.height])
		self.image = Maps[game.level-1]
		self.rect = self.image.get_rect()
		self.rect.y = self.y
		self.rect.x = self.x



class cazador(pygame.sprite.Sprite):
		def __init__(self,game,x,y):

			self.game = game
			self._layer = PLAYER_LAYER
			self.groups = self.game.all_sprites
			
			pygame.sprite.Sprite.__init__(self,self.groups)

			self.x = x * TPIXEL
			self.y = y * TPIXEL
			self.width = TPIXEL
			self.height = TPIXEL
			self.health = 50
			#self.hitbox = (self.x, self.y, PLAYER_HITBOX)
			self.hitbox = pygame.Rect(self.x, self.y, PLAYER_HITBOX[0], PLAYER_HITBOX[1])

			#estas son variables temporales que almacenan el cambio de movimientos dentro del ciclo
			self.x_change = 0
			self.y_change = 0

			self.facing = 'down' #posicion predeterminada de nuestro personaje

			self.image = pygame.Surface([self.width, self.height]) # creamos un rectangulo como la imagen de nuestro jugador
			#what it looks like
			self.image.fill(RED)

			self.rect = self.image.get_rect()# donde esta posisionado / hitbox / se hace del mismo tamaño que la imagen anteriormente definida
			self.rect.x = self.x
			self.rect.y = self.y
			#funcion actualizar movimiento

		def getHitbox(self):
			return self.hitbox


		def update(self):
			self.movement()
			self.rect.x += self.x_change
			self.rect.y += self.y_change
			#funcion de movimiento de personaje
			self.x_change = 0
			self.y_change = 0
		def movement(self):
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				self.x_change -= PLAYER_SPEED
				self.facing = 'left'
			if keys[pygame.K_RIGHT]:
				self.x_change += PLAYER_SPEED
				self.facing = 'right'
			if keys[pygame.K_UP]:
				self.y_change -= PLAYER_SPEED
				self.facing = 'up'
			if keys[pygame.K_DOWN]:
				self.y_change += PLAYER_SPEED
				self.facing = 'down'
			self.hitbox = (self.rect.x, self.rect.y, PLAYER_HITBOX[0], PLAYER_HITBOX[1])
		
		

					


class enemy(pygame.sprite.Sprite):
		def __init__(self,game,x,y):
    			
				self.game = game
				self._layer = ENEMY_LAYER
				self.groups = self.game.all_sprites, self.game.enemies
				pygame.sprite.Sprite.__init__(self,self.groups)


				self.x = x * ENEMYPIXEL
				self.y = y * ENEMYPIXEL
				self.width = ENEMYPIXEL
				self.height = ENEMYPIXEL

				self.y_change = 0
				self.x_change = 0

				self.health = 50
				surface = pygame.display.set_mode((400,300))
				self.rect=pygame.draw.rect(surface,BlACK, pygame.Rect(x,y,self.width,self.height))
				pygame.display.flip()
				
				
				self.rect.x = self.x
				self.rect.y = self.y

		def move_towards_player(self, player):
			# Find direction vector (dx, dy) between enemy and player.
			dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
			dist = math.hypot(dx, dy)
			dx, dy = dx / dist, dy / dist  # Normalize.
			# Move along this normalized vector towards the player at current speed.
			self.rect.x += dx * self.ENEMY_SPEED
			self.rect.y += dy * self.ENEMY_SPEED

			
				
		def update(self):
				self.rect.x += self.x_change
				self.rect.y += self.y_change

				self.x_change = 0
				self.y_change = 0


