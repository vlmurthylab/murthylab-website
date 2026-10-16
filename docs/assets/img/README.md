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

## PNG renders

Ready-made PNGs for avatars, slides, and anywhere SVG isn't accepted, each at
500px (GitHub's recommended avatar size) and 1024px:

    avatar-*.png        logo-circle artwork on a full-bleed #12161C square —
                        use this for the GitHub organization avatar or other
                        profile pictures; it survives both rounded-square and
                        circle crops
    logo-circle-*.png   logo-circle.svg, transparent corners
    logo-*.png          logo.svg on transparent, padded so no points clip
    logo-dark-*.png     logo-dark.svg on transparent, same padding
