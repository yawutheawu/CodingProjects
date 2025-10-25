extends Node3D

@export var move_speed: float = 1.0
@export var turn_speed: float = 1.0
@export var ground_offset: float = 0.3

@onready var front_right_target = $"SpiderRig/Front Right Target"
@onready var back_left_target = $"SpiderRig/Back Left Target"
@onready var back_right_target = $"SpiderRig/Back Right Target"
@onready var front_left_target = $"SpiderRig/Front Left Target"

@onready var player: CharacterBody3D = $"../Player"
@onready var NavAgent = $NavigationAgent3D
var openChest = false
func _process(delta):
	var plane1 = Plane(back_left_target.global_position, front_left_target.global_position, front_right_target.global_position)
	var plane2 = Plane(front_right_target.global_position, back_right_target.global_position, back_left_target.global_position)
	var avg_normal = ((plane1.normal + plane2.normal)/2).normalized()
	
	var target_basis = _basis_from_normal(avg_normal)
	transform.basis = lerp(transform.basis, target_basis, move_speed * delta).orthonormalized()
	
	var avg = (front_left_target.position + front_right_target.position + back_left_target.position + back_right_target.position)/4
	var target_pos = avg + transform.basis.y * ground_offset
	var distance = transform.basis.y.dot(target_pos-position)
	position = lerp(position, position + transform.basis.y * distance, move_speed*delta)
	
	movement(delta)

func movement(delta):
	NavAgent.set_target_position(player.position)
	var destination = NavAgent.get_next_path_position()
	var local_destination = destination - global_position
	var dir = local_destination.normalized()
	
	translate(Vector3(dir[0],0,dir[2])*move_speed*delta)
	
	#var a_dir = global_position.direction_to(player.global_position)
	#print(a_dir)
	#rotate_object_local(Vector3.UP,-(a_dir[1]-0.5) * turn_speed * delta)
	print(local_destination)
	if abs(local_destination[0]) > 1.5 and abs(local_destination[2]) > 1.5:
		$SpiderRig.look_at(player.global_position)
	
func _basis_from_normal(normal : Vector3) -> Basis:
	var result = Basis()
	result.x = normal.cross(transform.basis.z)
	result.y = normal
	result.z = transform.basis.x.cross(normal)
	
	result = result.orthonormalized()
	result.x *= scale.x
	result.y *= scale.y
	result.z *= scale.z
	
	return result


func _on_player_jumped():
	openChest = true
	print("Jumped (from the spider)")
