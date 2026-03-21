extends Area3D
var instance = preload("res://scenes/falling.tscn")
var falling_instance = null
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	
	pass


func _on_body_entered(body: Node3D) -> void:
	if falling_instance == null:
		$"../Timer".start()
		$CSGBox3D7["visible"] = false
		$"."["monitoring"] = false
		$CSGBakedCollisionShape3D["disabled"] = true
		$CSGBox3D7["use_collision"] = false
		falling_instance = instance.instantiate()
		$"..".add_child(falling_instance)
		falling_instance.global_position = $"..".global_position


func _on_timer_timeout() -> void:
	$CSGBox3D7["visible"] = true
	$CSGBakedCollisionShape3D["disabled"] = false
	$CSGBox3D7["use_collision"] = true
	$"."["monitoring"] = true
	#if (not is_instance_valid(falling_instance) or falling_instance.is_queued_for_deletion()) and falling_instance != null:
	falling_instance.queue_free()
	falling_instance = null
