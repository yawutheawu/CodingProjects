extends Node3D

@export var stairCount = 360

var vertOffset = 0.05
var horOffset = 0.1
var rot = 10
var count = 0
var previousNode = null

func _ready():
	var rootNode = $"."
	var previousNode = $"."
	for i in range(stairCount):
		var stairObj = preload("res://Scenes/stair.tscn").instantiate()
		rootNode.add_child(stairObj)
		stairObj.name = "Stair_%d" % count
		stairObj.position = previousNode.position
		stairObj.rotation = Vector3(stairObj.rotation.x,previousNode.rotation.y + rot,stairObj.rotation.z)
		stairObj.position = Vector3(stairObj.position.x + horOffset,stairObj.position.y + vertOffset, stairObj.position.z)
		previousNode = stairObj
		count += 1
