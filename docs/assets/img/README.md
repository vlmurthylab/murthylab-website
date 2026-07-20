# Logo assets

    logo.svg          primary mark, for light backgrounds
    logo-dark.svg     for dark backgrounds — cyan and violet lightened
    logo-circle.svg   contained lockup, for avatars and slide corners
    favicon.svg       simplified for 16–32px, fewer points, heavier strokes

All are vector and scale to any size. For a raster version:

    rsvg-convert -w 1200 logo.svg > logo@1200.png
    inkscape logo.svg -w 1200 -o logo@1200.png

## Colors

    vessel, light bg   #12161C
    vessel, dark bg    #F7F6F3
    distal segment     #C87F32   amber, both backgrounds
    molecular points   #3E7C8C   light bg
                       #5FA3B5   dark bg
    accent points      #6B5B7B   light bg
                       #8C7BA0   dark bg

The header mark is inlined in the HTML rather than linked, so it inherits text
color and switches automatically. Its colors come from the --mark-amber,
--mark-cyan, and --mark-violet variables in main.css.
