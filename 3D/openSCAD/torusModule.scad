module torus(radius = 5, thickness = 1, resolution = 100){
    rotate_extrude($fn=resolution, convexity=10)
    translate ([radius,0,0]) circle(thickness, $fn = resolution);
    
}

torus(15,5,150);