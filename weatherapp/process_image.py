def get_image(id):
    my_img = None

    if(id >= 200  and id <= 232 ):
        my_img = 'images/icons/icon-12.svg'

    elif (id >= 300 and id <= 321) or (id >= 520 and id <= 531):
        my_img = 'images/icons/icon-11.svg'

    elif id >= 500 and id <= 504:
        my_img = 'images/icons/icon-4.svg'

    elif (id >= 600 and id <= 622) or id == 511:
        my_img = 'images/icons/icon-7.svg'

    elif id >= 701 and id <= 781:
        my_img = 'images/icons/icon-8.svg'

    elif id >= 300 and id <= 321:
        my_img = 'images/icons/icon-6.svg'

    elif id == 801:
        my_img = 'images/icons/icon-3.svg'
    
    elif id == 800:
        my_img = 'images/icons/icon-2.svg'

    elif id >= 802 and id <= 804:
        my_img = 'images/icons/icon-6.svg'
    
    else:
        my_img = 'images/icons/icon-2.svg'

    return my_img