extends RigidBody3D
var speed = -25
# Called when the node enters the scene tree for the first time.
func _shoot(shootDirection):
	print(shootDirection*speed)
	apply_force(shootDirection*speed)
