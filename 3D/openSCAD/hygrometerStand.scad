/* [Hygrometer Holder] */

//Diameter of  he hygrometer in mm
hygrometerDiameter = 41.2;

//Desired thickness of hygrometer holding ring in mm
holderWallThickness = 10;

//Depth of the hygrometer in mm (or just the section that should be enveloped)
holderDepth = 10;

//Hygrometer Angle
holderAngle = 45; // [0:90]

/* [Base] */
//Vertical Thickness of holder base in mm
baseThickness = 5;

filletSize = 6;

/* [Post] */

//Height of the post from the top of the base
postHeight = 35;

//Thickness (radius) of the post
postRadius = 7;

//Faces used to render the post (4 for a square etc.)
postQuality = 12; // [4:100]



// Modules:
module torus(radius = 5, thickness = 1, resolution = 55){
    rotate_extrude($fn=resolution, convexity=10)
    translate ([radius,0,0]) circle(thickness > radius ? radius : thickness, $fn = resolution);
    
}

difference() {
    difference() {
        union() {
            //hoop
            translate([-(sin(90 - holderAngle) * (hygrometerDiameter/2 + holderWallThickness/2)),0,-((hygrometerDiameter/2 + holderWallThickness) - (cos(90 -  holderAngle) * (hygrometerDiameter/2 + holderWallThickness)))]) 
            translate([-holderDepth/2,0,hygrometerDiameter/2 + baseThickness + postHeight + holderWallThickness]) 
            rotate([0,holderAngle,0])  rotate_extrude(angle=360,convexity=10,$fn=85) 
            translate([hygrometerDiameter/2,0,0]) square([10,holderDepth]);

            // extrapost
            rotate([0,0,45]) 
            translate([0,0,baseThickness+postHeight]) 
            cylinder(
                h = ( holderAngle > 0 ? sin(holderAngle) * (holderDepth + (tan(90-holderAngle)  * holderWallThickness)) : holderDepth), 
                r = postRadius,$fn = postQuality);
        }
        translate([-(sin(90 - holderAngle) * (hygrometerDiameter/2 + holderWallThickness/2)) - holderDepth * cos(90-holderAngle),0,-((hygrometerDiameter/2 + holderWallThickness) - (cos(90 -  holderAngle) * (hygrometerDiameter/2 + holderWallThickness))) - holderDepth * sin(90-holderAngle)]) 
        translate([-holderDepth/2,0,hygrometerDiameter/2 + baseThickness + postHeight + holderWallThickness]) 
        rotate([0,holderAngle,0])  cylinder(h = holderDepth*2 + postRadius, r = hygrometerDiameter/2,$fn=85);
    }
    translate([-(sin(90 - holderAngle) * (hygrometerDiameter/2 + holderWallThickness/2)) + holderDepth * cos(90-holderAngle),0,-((hygrometerDiameter/2 + holderWallThickness) - (cos(90 -  holderAngle) * (hygrometerDiameter/2 + holderWallThickness))) + holderDepth * sin(90-holderAngle)]) 
    translate([-holderDepth/2,0,hygrometerDiameter/2 + baseThickness + postHeight + holderWallThickness]) 
    rotate([0,holderAngle,0])  cylinder(h = holderDepth, r = hygrometerDiameter/2 + holderWallThickness*1.5 + postRadius,$fn=85);
}
// Holder Construction

union() {
    //base
    translate([0,0,baseThickness/2]) 
    rotate([0,0,45]) 
    cylinder(
        h=baseThickness,
        r1=(hygrometerDiameter*1.2 + holderWallThickness + baseThickness*2)/sqrt(2), 
        r2 = (hygrometerDiameter*1.2 + holderWallThickness)/sqrt(2),center=true, $fn = 4);

    //post
    rotate([0,0,45]) translate([0,0,baseThickness]) cylinder(h = postHeight, r = postRadius, $fn = postQuality);

    //fillet
    difference() {
        difference() {
            translate([0,0,baseThickness + filletSize/2]) cube([postRadius*3,postRadius*3,filletSize],center=true);
            translate([0,0,baseThickness + (filletSize > postRadius ? postRadius : filletSize)/1.03]) torus(radius = postRadius + (filletSize > postRadius ? postRadius : filletSize)/sqrt(1.8), thickness = filletSize*1.089);
        }
        translate([0,0,baseThickness + filletSize]) rotate_extrude() translate([postRadius + filletSize*1.5,0,0]) square(filletSize*2,center=true);
    }
}