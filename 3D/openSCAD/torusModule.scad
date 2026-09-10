module torus(radius = 5, thickness = 1, resolution = 100){
    rotate_extrude($fn=resolution/2 > 5 ? resolution/2 < 50 ? resolution :  50 : 5, convexity=2)
    translate ([radius,0,0]) circle(thickness, $fn = resolution > 5 ? resolution < 100 ? resolution :  100 : 5);
    
}

torus(15,5);