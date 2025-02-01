extends Node2D

const SPEED = 40

var direction = 1

@onready var rightCheck = $RayCastRight
@onready var leftCheck = $RayCastLeft
@onready var aniSprite = $AnimatedSprite2D

func _process(delta):
	if rightCheck.is_colliding():
		direction = -1
		aniSprite.flip_h = true
	if leftCheck.is_colliding():
		direction = 1
		aniSprite.flip_h = false
	position.x += direction * SPEED * delta
