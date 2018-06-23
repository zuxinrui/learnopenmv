# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor, image, time

threshold_1 = (0, 35, 0, 50, -10, 40) # change this to condict the threshold

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
sensor.set_auto_whitebal(False)
clock = time.clock()                # Create a clock object to track the FPS.

while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()         # Take a picture and return the image.
    blobs = img.find_blobs([threshold_1], area_threshold=150)
    if blobs:
        print(blobs)
        for b in blobs:
            img.draw_rectangle(b[0:4])
            img.draw_cross(b[5], b[6])

    print(clock.fps())              # Note: OpenMV Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.
