/* [Hygrometer Holder] */

//Diameter of  he hygrometer in mm
hygrometerDiameter = 41.2;

//Desired thickness of hygrometer holding ring in mm
holderWallThickness = 10;

//Depth of the hygrometer in mm (or just the section that should be enveloped)
holderDepth = 10;

//Hygrometer Angle

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
postQuality = 8; // [4:100]



// Modules:
module torus(radius = 5, thickness = 1, resolution = 55){
    rotate_extrude($fn=resolution, convexity=10)
    translate ([radius,0,0]) circle(thickness > radius ? radius : thickness, $fn = resolution);
    
}



// Holder Construction

union() {
    //base
    translate([0,0,baseThickness/2]) 
    rotate([0,0,45]) 
    cylinder(
        h=baseThickness,
        r1=(hygrometerDiameter + holderWallThickness + baseThickness*2)/sqrt(2), 
        r2 = (hygrometerDiameter + holderWallThickness)/sqrt(2),center=true, $fn = 4);

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