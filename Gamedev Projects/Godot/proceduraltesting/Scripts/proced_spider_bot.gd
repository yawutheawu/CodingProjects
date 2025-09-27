extends Node3D

@export var move_speed: float = 5.0
@export var turn_speed: float = 1.0
@export var ground_offset: float = 0.3

@onready var front_right_target = $"SpiderRig/Front Right Target"
@onready var back_left_target = $"SpiderRig/Back Left Target"
@onready var back_right_target = $"SpiderRig/Back Right Target"
@onready var front_left_target = $"SpiderRig/Front Left Target"


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
	var dir = Input.get_axis("ui_down","ui_up")
	translate(Vector3(0,0,-dir)*move_speed*delta)
	
	var a_dir = Input.get_axis("ui_right","ui_left")
	rotate_object_local(Vector3.UP,a_dir * turn_speed * delta)
	
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
	
