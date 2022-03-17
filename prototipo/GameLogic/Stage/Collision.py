class Collision:
    def __init__(self):
        pass

    def check( object_1, object_2):
        top_left_x_1 = object_1.x_position
        top_left_y_1 = object_1.y_position
        bottom_left_y_1 = object_1.y_position + object_1.hitbox_y
        top_right_x_1 = object_1.x_position + object_1.hitbox_x

        top_left_x_2 = object_2.x_position
        top_left_y_2 = object_2.y_position
        bottom_left_y_2 = object_2.y_position + object_2.hitbox_y
        top_right_x_2 = object_2.x_position + object_2.hitbox_x

        if bottom_left_y_1 <= top_left_y_2:
            return False
        
        if top_left_y_1 >= bottom_left_y_2 :
            return False

        if top_right_x_1 <= top_left_x_2:
            return False

        if top_left_x_1 >= top_right_x_2:
            return False

        return True
