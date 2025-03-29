extends CharacterBody3D

# How fast the player moves in meters per second.
@export var speed = 14
# The downward acceleration when in the air, in meters per second squared.
@export var fall_acceleration = 75
#jump force
@export var jumpForce = 15

var target_velocity = Vector3.ZERO

var airtime = 250
var lastJump = -250

func _physics_process(delta):
	var direction = Vector3.ZERO

	if Input.is_action_pressed("ui_right"):
		direction.x -= 1
	if Input.is_action_pressed("ui_left"):
		direction.x += 1
	if Input.is_action_pressed("ui_down"):
		direction.z -= 1
	if Input.is_action_pressed("ui_up"):
		direction.z += 1
	if Input.is_action_pressed("ui_accept") and is_on_floor():
		direction.y += 1
		lastJump = Time.get_ticks_msec()
	if direction != Vector3.ZERO:
		direction = direction.normalized()
		#$Pivot.basis = Basis.looking_at(direction)

	# Ground Velocity
	print(target_velocity)
	target_velocity.x = direction.x * speed
	target_velocity.z = direction.z * speed
	target_velocity.y = target_velocity.y + direction.y * jumpForce
	# Vertical Velocity
	if not is_on_floor() and (Time.get_ticks_msec() > (lastJump + airtime)): # If in the air, fall towards the floor. Literally gravity
		target_velocity.y = target_velocity.y - (fall_acceleration * delta)
	elif not is_on_floor() and (Time.get_ticks_msec() < (lastJump + airtime)):
		direction.y += 1
		target_velocity.y = direction.y * jumpForce
	print(target_velocity)
	# Moving the Character
	velocity = target_velocity
	move_and_slide()
