extends Area3D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass 


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_body_entered(body: Node3D) -> void:
	if body.name == "Player":
		$Timer.start()
		print("body deteced")
		$Timer2.start()

func _on_timer_timeout() -> void:

	$"Platform 8"["visible"] = false
	$"Platform 8"["use_collision"] = false
	



func _on_timer_2_timeout() -> void:
	print("respawning")
	$"Platform 8"["visible"] = true
	$"Platform 8"["use_collision"] = true
