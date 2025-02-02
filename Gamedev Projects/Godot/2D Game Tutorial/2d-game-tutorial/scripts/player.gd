extends CharacterBody2D

# https://www.youtube.com/watch?v=LOhfqjmasi0

const SPEED = 130.0
const JUMP_VELOCITY = -300.0

var airtime = 0
var flag = false

@onready var aniSprite = $AnimatedSprite2D

func _physics_process(delta: float) -> void:

	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta
	
	if not is_on_floor() and flag == false:
		flag = true
		airtime = Engine.get_frames_drawn()
	
	if is_on_floor():
		airtime = 0
		flag = false
	# Handle jump
	
	if (Input.is_action_just_pressed("ui_accept") or Input.is_action_just_pressed("ui_up")) and (is_on_floor() or (Engine.get_frames_drawn()-airtime) < 3):
		$"Jump Noise".play()
		velocity.y = JUMP_VELOCITY

	var direction := Input.get_axis("ui_left", "ui_right")
	if Globals.Death == false:
		if direction > 0:
			aniSprite.flip_h= false
			aniSprite.play("Run")
		elif  direction < 0:
			aniSprite.flip_h = true
			aniSprite.play("Run")
		
		if direction == 0:
			aniSprite.play("Idle")

		if not is_on_floor() and (velocity.y < 0):
			aniSprite.play("Jump")
		elif not is_on_floor() and (velocity.y > 0):
			aniSprite.play("Fall")
	
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)

	move_and_slide()
