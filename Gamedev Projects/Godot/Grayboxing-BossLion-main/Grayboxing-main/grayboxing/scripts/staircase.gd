extends Node


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	var spacing = 0.1
	var count = 0
	var start_point = 3.9
	var rotation_deg = 1
	var h_move = 0.05
	for i in get_children():
		#i.rotation = Vector3(i.rotation.x, i.rotation.y + (rotation_deg *count), i.rotation.z)
		i.position = Vector3(i.position.x + (h_move * count),start_point + (spacing * count),i.position.z)
		i.scale = Vector3(1,1,1)
		count += 1 


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
