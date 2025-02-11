extends CharacterBody3D
@export var bullet_scene = preload("res://Scenes/bullet.tscn")
# Character movement constants
const SPEED = 5.0
const JUMP_VELOCITY = 4.5

# Track mouse capture state
var is_mouse_captured = false  # Set this to false by default

# Sensitivity for mouse movement
var sensitivity = 0.1

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
		# Calculate rotation based on mouse movement and sensitivity
		var rotation_delta = event.relative * sensitivity
		
		# Rotate around the Y-axis (horizontal) and X-axis (vertical)
		rotation_degrees.y -= rotation_delta.x  # Horizontal rotation
		rotation_degrees.x -= rotation_delta.y  # Vertical rotation
		rotation_degrees.x = clamp(rotation_degrees.x, -90, 90)  # Limit vertical rotation to avoid flipping
	
func check_for_shooting():
	if Input.is_action_pressed("shoot"):
		shoot()

func shoot():
	var bullet_instance = bullet_scene.instantiate()
	get_tree().root.add_child(bullet_instance) # add the projectile
	
	bullet_instance.global_transform = $ProjectileSpawnPoint.global_transform
	bullet_instance._shoot($Camera3D.get_global_transform().basis.z)
	#print($Camera3D.get_global_transform().basis.z)
# Function to process input events
func _input(event: InputEvent) -> void:
	# Call mouse movement handler
	check_for_shooting()
	_mouse_movement(event)
	# Also check for mouse capture/release
	_capture_release_mouse_button()
