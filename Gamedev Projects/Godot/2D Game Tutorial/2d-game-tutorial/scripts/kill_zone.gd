extends Area2D

@onready var timer: Timer = $Timer

func _on_body_entered(body: Node2D) -> void:
	Engine.time_scale = 0.3
	body.velocity.y = -150.0
	gravity *= 5
	body.get_node("CollisionShape2D").queue_free()
	timer.start()


func _on_timer_timeout() -> void:
	gravity /= 5
	Engine.time_scale = 1
	get_tree().reload_current_scene()
