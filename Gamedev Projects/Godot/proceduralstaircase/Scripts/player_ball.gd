extends Node3D

var lastPos = null
var currentPos = null

func _process(delta):
	if currentPos == null:
		currentPos = $RigidBody3D.global_position
		lastPos = currentPos
	lastPos = currentPos
	currentPos = $RigidBody3D.global_position
	var direction = (currentPos - lastPos).normalized()
	$Camera3D.global_position = $RigidBody3D.global_position
	#$Camera3D.global_rotation = $RigidBody3D.global_rotation
	$Camera3D.global_rotation.x = lerp_angle($Camera3D.global_position.x, ($Camera3D.global_position.x + direction.x), 2.5*delta)
	$Camera3D.global_rotation.y = lerp_angle($Camera3D.global_position.y, ($Camera3D.global_position.y + direction.y), 2.5*delta)
	$Camera3D.global_rotation.z = lerp_angle($Camera3D.global_position.z, ($Camera3D.global_position.z + direction.z), 2.5*delta)
	#$Camera3D.global_rotation.z = 0
	#$Camera3D.look_at($Camera3D.global_position + direction)
