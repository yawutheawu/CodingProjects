extends CharacterBody3D
# Character movement constants
var SPEED = 5.0
var WALK_SPEED = 5.0
var SPRINT_SPEED = 7.0
const JUMP_VELOCITY = 4.5
var jump = 0
var gravity_flip_unlock = false
# Track mouse capture state
var is_mouse_captured = false  # Set this to false by default
var gravity_direction = 1
# Sensitivity for mouse movement
var sensitivity = 0.1
var tweenTime = 0.75


func gravity_flip():
	if gravity_direction > 0:
		return is_on_floor()
	else:
		return is_on_ceiling()

signal addWood(wood: int)

# Physics process (Character movement)
func _physics_process(delta: float) -> void:
	var tween = get_tree().create_tween().set_ease(Tween.EASE_IN).set_parallel(true)
	var tweenUpsideDown = get_tree().create_tween().set_ease(Tween.EASE_IN).set_parallel(true)
	var tweenRightsideUp = get_tree().create_tween().set_ease(Tween.EASE_IN).set_parallel(true)
	tween.tween_property($".", "velocity:y", 0, tweenTime)
	tween.stop()
	tweenUpsideDown.tween_property($".", "rotation:z", deg_to_rad(180), tweenTime)
	tweenUpsideDown.stop()
	tweenRightsideUp.tween_property($".", "rotation:z", 0, tweenTime)
	tweenRightsideUp.stop()
	if gravity_direction < 0:
		tweenUpsideDown.play()
	else:
		tweenRightsideUp.play()
	# Add gravity if not on the floor
	if not gravity_flip():
		velocity += get_gravity() * delta * gravity_direction
	if Input.is_action_just_pressed("gravity_flip") and gravity_flip_unlock:
		gravity_direction *= -1
		tween.play()
		
		
	if gravity_flip():
		jump = 0
	# Handle jump input
	if Input.is_action_just_pressed("ui_accept") and jump <= 1:
		if jump == 0:
			velocity.y = JUMP_VELOCITY * gravity_direction
		else:
			velocity.y += JUMP_VELOCITY * gravity_direction
		jump += 1

	# Get input direction and handle movement
	var input_dir := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	var direction := (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	if direction:
		velocity.x = direction.x * SPEED
		velocity.z = direction.z * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		velocity.z = move_toward(velocity.z, 0, SPEED)
	move_and_slide()

	# Check every frame if mouse capture/release worked
	_capture_release_mouse_button()

# Mouse capture/release handling
func _capture_release_mouse_button():
	if Input.is_action_just_pressed("mouse_middle"):
		capture_mouse()
	
	if Input.is_action_just_pressed("release_mouse"):
		release_mouse()

# Function to release mouse capture
func release_mouse():
	Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	is_mouse_captured = false
	print("Mouse Released: ", is_mouse_captured)

# Function to capture the mouse
func capture_mouse():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	is_mouse_captured = true
	print("Mouse Captured: ", is_mouse_captured)

# Mouse movement handling (Rotation)
func _mouse_movement(event: InputEvent) -> void:
	if event is InputEventMouseMotion:
		# Correct Horizontal Mouse Movement when Gravity is flipped
		rotate_y(deg_to_rad(-event.relative.x*sensitivity*gravity_direction))
		$Node3D.rotate_x(deg_to_rad(-event.relative.y*sensitivity))# Limit vertical rotation to avoid flipping
		$Node3D.rotation_degrees.x = clamp($Node3D.rotation_degrees.x,-90,90)
func sprint():
	if Input.is_action_just_pressed("shift"):
		SPEED = SPRINT_SPEED
	if Input.is_action_just_released("shift"):
		SPEED = WALK_SPEED
		
func _on_item_collected(item_node):
	var item_holder = get_node("ItemHolder")
	item_node.reparent(item_holder)
	

func _input(event: InputEvent) -> void:
	# Call mouse movement handler
	#check_for_shooting()
	_mouse_movement(event)
	sprint()
	# Also check for mouse capture/release
	_capture_release_mouse_button()
