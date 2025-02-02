extends Area2D
@onready var animated_sprite_2d: AnimatedSprite2D = $AnimatedSprite2D
@onready var animation_player: AnimationPlayer = $AnimationPlayer

var rng = RandomNumberGenerator.new()
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	animated_sprite_2d.frame = rng.randi_range(0, animated_sprite_2d.sprite_frames.get_frame_count(animated_sprite_2d.animation))



func _on_body_entered(_body: Node2D) -> void:
	%"Game Manager".add_point()
	animation_player.play("Pickup")
