from basic_computations      import calculate_circle_xy_coordinates

circular_magnet_radius                     = 6.0
rectangle_magnet_width                     = 12.0
rectangle_magnet_length                    = 20.0
circular_rectangle_magnet_distance         = 23.0
circular_rectangle_magnet_center_distance  = (circular_magnet_radius + circular_rectangle_magnet_distance
                                              + rectangle_magnet_length / 2.0)
HECTOR_plate                               = calculate_circle_xy_coordinates(0.0,0.0,260.0)
robot_arm_length                           = 14.02
robot_arm_width                            = 5
circular_magnet_pickuparea_length          = robot_arm_length
circular_magnet_pickuparea_width           = (3.0 * robot_arm_width / 2.0) + circular_magnet_radius
rectangle_magnet_pickuparea_length         = robot_arm_length
rectangle_magnet_pickuparea_width          = 0.5 * (rectangle_magnet_length + 3.0 * robot_arm_width)