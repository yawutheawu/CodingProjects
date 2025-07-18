extends CharacterBody3D

@onready var player: CharacterBody3D = $"../Player"
@onready var NavAgent = $NavigationAgent3D
var SPEED = 0.5



func _physics_process(_delta):
	NavAgent.set_target_position(player.position)
	var destination = NavAgent.get_next_path_position()
	var local_destination = destination - global_position
	var direction = local_destination.normalized()
	
	velocity = direction * SPEED
	
	move_and_slide()


func _on_navigation_agent_3d_velocity_computed(safe_velocity):
	velocity = safe_velocity # Replace with function body.
