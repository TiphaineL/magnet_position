def rect_rect_intersection(x_1,y_1,ang_1,l_1,w_1,x_2,y_2,ang_2,l_2,w_2):
### check the intersection of a rectangle with a rectangle, by iterating through every pair of segments from rectangle 1
### and of rectangle 2
### with x_1/2 and y_1/2 the coordinates of the center of the rectangle 1/2, ang_1/2 the orientation of the rectangle
### (along the vertical axis), l_1/2 and w_1/2 the length and width of the rectangle 1/2

    from rect_corner import rectangle_corner
    from segment_segment_intersection import segments_intersection

    # Calculate the coordinates of the corners of the rectangle (4 corners)
    corner_rect_1 = rectangle_corner(x_1,y_1,l_1,w_1,ang_1)
    corner_rect_2 = rectangle_corner(x_2,y_2,l_2,w_2,ang_2)

    inter = False
    for k,l in zip([0,1,2,3],[1,2,3,0]):
        for m,n in zip([0,1,2,3],[1,2,3,0]):

            x1 = corner_rect_1[k][0]
            y1 = corner_rect_1[k][1]

            x2 = corner_rect_1[l][0]
            y2 = corner_rect_1[l][1]

            x3 = corner_rect_2[m][0]
            y3 = corner_rect_2[m][1]

            x4 = corner_rect_2[n][0]
            y4 = corner_rect_2[n][1]

            intersection = segments_intersection(x1,y1,x2,y2,x3,y3,x4,y4)

            if intersection == True:
                inter = True

    return inter