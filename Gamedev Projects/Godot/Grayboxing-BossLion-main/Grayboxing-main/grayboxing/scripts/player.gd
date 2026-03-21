extends CharacterBody3D
# Character movement constants
var SPEED = 5.0
var WALK_SPEED = 5.0
var SPRINT_SPEED = 10.0
const JUMP_VELOCITY = 4.5
var wood = 0
# Track mouse capture state
var is_mouse_captured = false  # Set this to false by default

# Sensitivity for mouse movement
var sensitivity = 0.1

signal addWood(wood: int)

# Physics process (Character movement)
func _physics_process(delta: float) -> void:
	# Add gravity if not on the floor
	if not is_on_floor():
		velocity += get_gravity() * delta

	# Handle jump input
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

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
		rotate_y(deg_to_rad(-event.relative.x*sensitivity))
		$Node3D.rotate_x(deg_to_rad(-event.relative.y*sensitivity))# Limit vertical rotation to avoid flipping
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
