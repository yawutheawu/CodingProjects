extends CharacterBody3D

@onready var NavAgent = $NavigationAgent3D
var SPEED = 0.5

func _physics_process(delta):
	NavAgent.set_target_position($"../../Player".position)
	var destination = NavAgent.get_next_path_position()
	var local_destination = destination - global_position
	var direction = local_destination.normalized()
	
	velocity = direction * SPEED 
	move_and_slide()
