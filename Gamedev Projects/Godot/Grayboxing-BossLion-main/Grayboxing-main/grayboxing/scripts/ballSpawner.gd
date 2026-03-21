extends Node3D
var instance = preload("res://scenes/ball.tscn")
var ball_instance = null

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	randomize()
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_timer_timeout() -> void:
	ball_instance = instance.instantiate()
	%BallSpawn.add_child(ball_instance)
	ball_instance.global_position = Vector3(%BallSpawn.global_position.x + randf_range(-4, 4),%BallSpawn.global_position.y,%BallSpawn.global_position.z)
