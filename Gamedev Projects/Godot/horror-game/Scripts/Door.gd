extends Area3D

func _on_body_entered(body):
	print("Door Touched")
	print(body.name)
	for i in range(0,100,0.5):
		$PivotPoin.rotation = Vector3(0,-deg_to_rad(i),0)
		$DoorCol.rotation = $PivotPoin/DoorMesh.rotation
		$DoorCol.global_position = $PivotPoin/DoorMesh.global_position
		await get_tree().create_timer(0.1).timeout
	$PivotPoin.rotation = Vector3(0,deg_to_rad(-99.0),0)
	$DoorCol.rotation = $PivotPoin/DoorMesh.rotation
	$DoorCol.global_position = $PivotPoin/DoorMesh.global_position

func _on_ready():
	print("AreaReady")
