$fa = 1;
$fs = 0.1;

translate([-225,0,0]) union() {
for (i=[0:0.1:360]) {
    translate([15 + i,15,0]) rotate(a=i,v=[1,1,1]) cube([10,10,10],center=true);
}
}


translate([-25,0,0]) sphere(10);

translate([10,-10,0]) rotate(a=90, v=[1,1,0]) cylinder(r1=5,r2=15,h=20);