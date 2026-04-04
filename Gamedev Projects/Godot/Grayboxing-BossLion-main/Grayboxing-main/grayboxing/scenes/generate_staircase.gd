extends Node3D
@export var steps = 3
@export var angle = 15.0
@export var stepWidth = 1.0
@export var stepHeight = 0.5

var currentSteps = 0
@onready var originalStep = preload("res://scenes/step.tscn")
@onready var lastStep = originalStep.instantiate()
var previousStep = null

func _on_ready():
	add_child(lastStep)
	lastStep.position = global_position
	currentSteps = 1



func _process(delta):
	while currentSteps < steps:
		print(lastStep.global_position)
		previousStep = lastStep
		lastStep = originalStep.instantiate()
		add_child(lastStep)
		lastStep.global_position = previousStep.global_position
		lastStep.global_rotation = previousStep.global_rotation
		lastStep.rotate_y(deg_to_rad(angle))
		lastStep.translate(-transform.basis.z * stepWidth)
		lastStep.translate(Vector3.UP * stepHeight)
		currentSteps += 1
		print(currentSteps,)
