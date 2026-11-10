import streamlit as st

import cv2 #Format Normalspeed ist 1080*1920, Format Slowmotion ist 720*1280,focal_length1_slowmotion=0.201054,focal_length2_slowmotion 0.221296, focal_length_normalspeed=0.228198, focal_length2_normalspeed=0.254061
import numpy as np
import math
import sympy as sp
from PIL import Image
#import pyvista as pv
import csv
import gdown
import time
from pathlib import Path

st.header("Segmentierungsverfahren")

col1, col2=st.columns(2)

with col1:
    video_nummer=st.number_input("Welches Video möchtest du analysiert haben (Nr. 4-17)?", min_value=4, max_value=17, value=4, step=1)
with col2:
    if st.button("🔄 Seite zurücksetzen"):
        st.session_state.clear()
        st.rerun()
start_segmentation2=None
stopp_segmentation2=None

def video_download(url, dateiname):
    pfad = Path(dateiname)

    if not pfad.exists():
        gdown.download(url, str(pfad), quiet=True)

    return str(pfad)


if video_nummer==4:
    url1="https://drive.google.com/file/d/1aOjvR1bF0PNR5lL5oG_PZaA6VmSV4rnt/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1Neae1Sc5-wCV-W9VN78X-Y9srm80QtJn/view?usp=drive_link"
    video1=video_download(url1, "A Axel normalspeed.mp4")
    video2=video_download(url2, "B Axel normalspeed.mp4")
    focal_length1=0.228198
    focal_length2=0.254061
    pixel_length=1920
    pixel_width=1080
    lower_blue1 = np.array([90, 240, 130])
    upper_blue1 = np.array([130, 255, 140])
    lower_blue2 = np.array([90, 240, 130])
    upper_blue2 = np.array([130, 255, 150])
    
    lower_green1 = np.array([40, 60, 50])#V60->50, S100->60
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 90, 100])#S100->90
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 90, 50])#V100->50, S100->90, H170->160
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 60, 40])#V60->40, S90->60
    upper_green2 = np.array([85, 255, 255])
    lower_red1_2 = np.array([0, 150, 30])#V40->30, S190->150
    upper_red1_2 = np.array([25, 255, 255])
    lower_red2_2 = np.array([170, 150, 30])#V40->30, S190->150
    upper_red2_2 = np.array([179, 255, 255])

    start_segmentation=550
    stopp_segmentation=630
    take_off_red=577
    take_off_green=577
    landing_red=590
    landing_green=590
    landingplane_green=None
    landingplane_red=-0.45
    take_off_plane_green=-0.24
    take_off_plane_red=None

elif video_nummer==5:
    url1="https://drive.google.com/file/d/1eTJMw48dRoMXxCFv5mdxYXIrUWDaFqMs/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1ifB3ByF153VGP5ITew4u_jFcMH-JQBoe/view?usp=drive_link"
    video1=video_download(url1, "A Axel slowmotion 1.mp4")
    video2=video_download(url2, "B Axel slowmotion 1.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([90, 240, 140])
    upper_blue1 = np.array([130, 255, 170])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    
    lower_green1 = np.array([40, 75, 75])#V100->75, S100->75
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2200
    stopp_segmentation=2300
    start_segmentation2=4400
    stopp_segmentation2=4600
    take_off_red=2230
    take_off_green=2230
    landing_red=2285
    landing_green=2285
    landingplane_green=None
    landingplane_red=-0.543
    take_off_plane_green=None
    take_off_plane_red=-0.476

elif video_nummer==6:
    url1="https://drive.google.com/file/d/1x4LKsktIsWw6jQcmKPtizQE8biV_waW2/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1IIPPaAremVEh_QuEfkQ7aMbf6kSK_TX3/view?usp=drive_link"
    video1=video_download(url1, "A Axel slowmotion 2.mp4")
    video2=video_download(url2, "B Axel slowmotion 2.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([90, 240, 140])
    upper_blue1 = np.array([130, 255, 190])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    
    lower_green1 = np.array([40, 75, 75])
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 50])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2300
    stopp_segmentation=2450
    start_segmentation2=4600
    stopp_segmentation2=4900
    take_off_red=2327
    take_off_green=2327
    landing_red=2383
    landing_green=2383
    landingplane_green=None
    landingplane_red=-0.541
    take_off_plane_green=None
    take_off_plane_red=-0.729


elif video_nummer==7:
    url1="https://drive.google.com/file/d/1yIwtgK2pn3v3QIV-ZBCk45dK6X1bWctr/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1UBVQxoZNyKT227yXiq1Bya5HzTrUuOU7/view?usp=drive_link"
    video1=video_download(url1, "A Salchow normalspeed.mp4")
    video2=video_download(url2, "B Salchow normalspeed.mp4")
    focal_length1=0.228198
    focal_length2=0.254061
    pixel_length=1920
    pixel_width=1080
    lower_blue1 = np.array([90, 240, 130])
    upper_blue1 = np.array([130, 255, 150])
    lower_blue2 = np.array([90, 240, 130])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 100, 60])
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 95, 50])#S100->95, V100->50
    upper_red1_1 = np.array([30, 255, 255])#H10->30
    lower_red2_1 = np.array([160, 95, 50])#H170->160, S100->95
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 140, 30])#S190->140
    upper_red1_2 = np.array([45, 255, 255])#H25->45
    lower_red2_2 = np.array([150, 140, 30])#S190->140, H170->150
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=630
    stopp_segmentation=710
    take_off_red=658
    take_off_green=658
    landing_red=669
    landing_green=669
    landingplane_green=-0.41
    landingplane_red=None
    take_off_plane_green=-0.264
    take_off_plane_red=None


elif video_nummer==8: #Hier kein Absprung und keine Landung->das Programm muss noch angepasst werden, dass es das ausgibt
    url1="https://drive.google.com/file/d/1HT-3bK7T-4z6eP0DeOdpETPjBoZiJ35s/view?usp=drive_link"
    url2="https://drive.google.com/file/d/138CL2K2JqPQME5nhYWvFiJopBteVVeLt/view?usp=drive_link"
    video1=video_download(url1, "A Salchow slowmotion 1.mp4")
    video2=video_download(url2, "B Salchow slowmotion 1.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([90, 240, 140])
    upper_blue1 = np.array([130, 255, 170])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 100, 100])
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 90])
    upper_red1_1 = np.array([10, 255, 255])
    lower_red2_1 = np.array([170, 100, 90])
    upper_red2_1 = np.array([179, 255, 255])
    lower_green2 = np.array([35, 90, 50])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 190, 30])
    upper_red1_2 = np.array([25, 255, 255])
    lower_red2_2 = np.array([170, 190, 30])
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2400
    stopp_segmentation=2700
    start_segmentation2=4800
    stopp_segmentation2=5400
    take_off_red=2600
    take_off_green=2600
    landing_red=None
    landing_green=None
    landingplane_green=None
    landingplane_red=None
    take_off_plane_green=None
    take_off_plane_red=None

elif video_nummer==9:
    url1="https://drive.google.com/file/d/1yfCuWxciPkKVeD29ufZSb9EdPovEczfV/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1SyVeKq6DPRC3Mx6uz3LsyMkb-o91wajI/view?usp=drive_link"
    video1=video_download(url1, "A Salchow slowmotion 2.mp4")
    video2=video_download(url2, "B Salchow slowmotion 2.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([70, 220, 140])
    upper_blue1 = np.array([130, 255, 255])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 75, 75])#V100->75, S100->75
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2150
    stopp_segmentation=2300
    start_segmentation2=4300
    stopp_segmentation2=4600
    take_off_red=2206
    take_off_green=2206
    landing_red=2245
    landing_green=2245
    landingplane_green=-0.382
    landingplane_red=-0.422
    take_off_plane_green=None
    take_off_plane_red=-0.764

elif video_nummer==10:
    url1="https://drive.google.com/file/d/14JqYIJSUqee-pM--Vo0jOIiu_fefTcmx/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1RS84ENZtY34UCNnr7KOhU39FLMwM74RS/view?usp=drive_link"
    video1=video_download(url1, "A Toeloop normalspeed.mp4")
    video2=video_download(url2, "B Toeloop normalspeed.mp4")
    focal_length1=0.228198
    focal_length2=0.254061
    pixel_length=1920
    pixel_width=1080
    lower_blue1 = np.array([90, 240, 120])
    upper_blue1 = np.array([130, 255, 130])
    lower_blue2 = np.array([90, 240, 130])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 100, 60])
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 50])#V100->50
    upper_red1_1 = np.array([30, 255, 255])#H10->30
    lower_red2_1 = np.array([160, 100, 50])#V100->50, H170->160
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 140, 30])#S190->140
    upper_red1_2 = np.array([45, 255, 255])#H25->45
    lower_red2_2 = np.array([150, 140, 30])#S190->140, H170->150
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=600
    stopp_segmentation=690
    take_off_red=611
    take_off_green=611
    landing_red=626
    landing_green=626
    take_off_plane_green=-0.42
    take_off_plane_red=-0.437
    landingplane_green=-0.45
    landingplane_red=-0.48


elif video_nummer==11:
    url1="https://drive.google.com/file/d/1lY6DRW58_lAJHcpfIJXxZqLzvFm3FCs1/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1yER3MJyAmZIhVRm6cJtPN1Mjko6VxTrZ/view?usp=drive_link"
    video1=video_download(url1, "A Toeloop slowmotion 1.mp4")
    video2=video_download(url2, "B Toeloop slowmotion 1.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([90, 240, 140])
    upper_blue1 = np.array([130, 255, 170])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 75, 75])#V100->75, S100->75
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2350
    stopp_segmentation=2500
    start_segmentation2=4700
    stopp_segmentation2=5000
    take_off_red=2489
    take_off_green=2489
    landing_red=2510
    landing_green=2510
    landingplane_green=-0.72
    landingplane_red=-0.73
    take_off_plane_green=-0.73
    take_off_plane_red=None

elif video_nummer==12:
    url1="https://drive.google.com/file/d/1EOG1zCgoANUkaureK2LN5syzjbytcfk-/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1aOCFxcflr2IZ0SImmKhX5Wu4hFife3U3/view?usp=drive_link"
    video1=video_download(url1, "A Toeloop slowmotion 2.mp4")
    video2=video_download(url2, "B Toeloop slowmotion 2.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([70, 220, 140])
    upper_blue1 = np.array([130, 255, 255])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 75, 75])#V100->75, S100->75
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2700
    stopp_segmentation=2850
    start_segmentation2=5400
    stopp_segmentation2=5700
    take_off_red=2752
    take_off_green=2752
    landing_red=2796
    landing_green=2796
    landingplane_green=-0.8
    landingplane_red=-0.84
    take_off_plane_green=-1
    take_off_plane_red=None

elif video_nummer==13:
    url1="https://drive.google.com/file/d/1Kvxsz7ERA_HbBvetP55aUUw9bxv615Pm/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1FieweKFFcJvva8rUmPxTkr2Wn7h70Bhv/view?usp=drive_link"
    video1=video_download(url1, "A Loop normalspeed.mp4")
    video2=video_download(url2, "B Loop normalspeed.mp4")
    focal_length1=0.228198
    focal_length2=0.254061
    pixel_length=1920
    pixel_width=1080
    lower_blue1 = np.array([90, 240, 130])
    upper_blue1 = np.array([130, 255, 150])
    lower_blue2 = np.array([90, 240, 130])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 80, 60])#S100->80
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 50])#V100->50
    upper_red1_1 = np.array([10, 255, 255])
    lower_red2_1 = np.array([170, 100, 50])#V100->50
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 140, 30])#S190->140
    upper_red1_2 = np.array([45, 255, 255])#H25->45
    lower_red2_2 = np.array([150, 140, 30])#S190->140, H170->150
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=800
    stopp_segmentation=895
    take_off_red=810
    take_off_green=810
    landing_red=822
    landing_green=822
    landingplane_green=None
    landingplane_red=-0.356
    take_off_plane_green=-0.4
    take_off_plane_red=-0.4459


elif video_nummer==14:
    url1="https://drive.google.com/file/d/1bLorzlGqHflEwQfdSK1HCYR5QlLAA6ag/view?usp=drive_link"
    url2="https://drive.google.com/file/d/13q0tonpxMpHVZLzM9C4D8PP33FIOm4k7/view?usp=drive_link"
    video1=video_download(url1, "A Loop slowmotion.mp4")
    video2=video_download(url2, "B Loop slowmotion.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([70, 210, 140])
    upper_blue1 = np.array([130, 255, 255])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 75, 75])#V100->75, S100->75
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2357
    stopp_segmentation=2550
    start_segmentation2=4714
    stopp_segmentation2=5100
    take_off_red=2372
    take_off_green=2372
    landing_red=2425
    landing_green=2425
    landingplane_green=None
    landingplane_red=-0.766
    take_off_plane_green=None
    take_off_plane_red=-0.675

elif video_nummer==15:
    url1="https://drive.google.com/file/d/1tVjhmdRTG6gUgbvrgCX4kU-qa8w40xGZ/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1_mjvKFBzpzEqvd3IfJXLGx6WmPE-Icni/view?usp=drive_link"
    video1=video_download(url1, "A Lutz normalspeed.mp4")
    video2=video_download(url2, "B Lutz normalspeed.mp4")
    focal_length1=0.228198
    focal_length2=0.254061
    pixel_length=1920
    pixel_width=1080
    lower_blue1 = np.array([90, 240, 130])
    upper_blue1 = np.array([130, 255, 150])
    lower_blue2 = np.array([90, 240, 130])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 100, 60])
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 50])#V100->50
    upper_red1_1 = np.array([10, 255, 255])
    lower_red2_1 = np.array([160, 100, 50])#V100->50, H170->160
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 140, 30])#S190->140
    upper_red1_2 = np.array([45, 255, 255])#H25->45
    lower_red2_2 = np.array([150, 140, 30])#S190->140,H170->150
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=550
    stopp_segmentation=630
    take_off_red=562
    take_off_green=562
    landing_red=575
    landing_green=575
    landingplane_green=-0.34
    landingplane_red=-0.373
    take_off_plane_green=-0.38
    take_off_plane_red=-0.4

elif video_nummer==16:
    url1="https://drive.google.com/file/d/1iSmq3-gpwOmSz-eGc8PmwRuHiGspxW2d/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1YkPucZJPSFw3cf02jpxzNqjoyecac8NQ/view?usp=drive_link"
    video1=video_download(url1, "A Lutz slowmotion 1.mp4")
    video2=video_download(url2, "B Lutz slowmotion 1.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([90, 220, 140])
    upper_blue1 = np.array([130, 255, 180])
    lower_blue2 = np.array([90, 240, 140])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 75, 75])#V100->75, S100->75
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=2200
    stopp_segmentation=2600
    start_segmentation2=4400
    stopp_segmentation2=5400
    take_off_red=2334
    take_off_green=2334
    landing_red=2388
    landing_green=2388
    landingplane_green=None
    landingplane_red=-0.812
    take_off_plane_green=-0.93
    take_off_plane_red=None

elif video_nummer==17:
    url1="https://drive.google.com/file/d/13QbLaVZXj9te37a__26Q3_hO-AihHj4y/view?usp=drive_link"
    url2="https://drive.google.com/file/d/1pFrxpMGDurdWYlfUVCqvAUFwsimzWIru/view?usp=drive_link"
    video1=video_download(url1, "A Lutz slowmotion 2.mp4")
    video2=video_download(url2, "B Lutz slowmotion 2.mp4")
    focal_length1=0.201054
    focal_length2=0.221296
    pixel_length=1280
    pixel_width=720
    lower_blue1 = np.array([90, 220, 140])
    upper_blue1 = np.array([130, 255, 180])
    lower_blue2 = np.array([90, 240, 130])
    upper_blue2 = np.array([130, 255, 150])
    lower_green1 = np.array([40, 75, 75])#V100->75, S100->75
    upper_green1 = np.array([70, 255, 255])
    lower_red1_1 = np.array([0, 100, 70])#V90->70
    upper_red1_1 = np.array([20, 255, 255])#H10->20
    lower_red2_1 = np.array([160, 100, 70])#H170->160, V90->70
    upper_red2_1 = np.array([179, 255, 255])

    lower_green2 = np.array([35, 90, 60])
    upper_green2 = np.array([85, 255, 200])
    lower_red1_2 = np.array([0, 170, 30])#190->170
    upper_red1_2 = np.array([30, 255, 255])#H25->30
    lower_red2_2 = np.array([165, 170, 30])#H170->165, S190->170
    upper_red2_2 = np.array([179, 255, 255])
    start_segmentation=3900
    stopp_segmentation=4200
    start_segmentation2=7800
    stopp_segmentation2=8400
    take_off_red=4055
    take_off_green=4055
    landing_red=4107
    landing_green=4107
    landingplane_green=-0.595
    landingplane_red=-0.618
    take_off_plane_green=None
    take_off_plane_red=-0.76
else:
    print("Dieses Video gibt es nicht!!!")



angle30 = math.radians(30)
handyA_eckpunkte=[[0,0,0.0628001],[0.117837,0.0068034,0.0628001],[0,0,0],[0.117837,0.0068034,0]] #obenlinks,obenrechts,untenlinks, untenrechts
handyB_eckpunkte=[[-5.1278224,0.073799,0.0681221],[-5,0,0.0681221],[-5.1278224,0.073799,0],[-5,0,0]]
focal_position1=[0.117837/2+math.sin(angle30)*focal_length1,0.068034/2-math.cos(angle30)*focal_length1,0.0628001/2]#Position des Brennpunktes berechnet im Koordinatensystem Kamera A
focal_position2=[-5-(0.127824/2)-math.sin(angle30)*focal_length2,0.073799-math.cos(angle30)*focal_length2,0.0681221/2]#Kamera B



def get_position_in_space1_normal(position_on_screen):
    left,upper,right,lower=position_on_screen
    midpoint_position_pixel=[(left+right)/2,pixel_width-((upper+lower)/2)] #Mittelpunkt von der segmentierten Stelle nehmen
    height_on_screen_m=midpoint_position_pixel[1]/pixel_width*0.0628001 #Umrechnen von Pixel in m auf dem Screen (von unten und von links)
    distance_from_left_side_m=midpoint_position_pixel[0]/pixel_length*0.136067
    angle = math.radians(30)
    position_in_space=[math.cos(angle)*distance_from_left_side_m,math.sin(angle)*distance_from_left_side_m,height_on_screen_m]
    return(position_in_space)

def get_position_in_space2_normal(position_on_screen): 
    left,upper,right,lower=position_on_screen
    midpoint_position_pixel=[(left+right)/2,pixel_width-((upper+lower)/2)] #Mittelpunkt von der segmentierten Stelle nehmen
    height_on_screen_m=midpoint_position_pixel[1]/pixel_width*0.0681221 #Umrechnen von Pixel in m auf dem Screen (von unten und von rechts)
    distance_from_right_side_m=(pixel_length-midpoint_position_pixel[0])/pixel_length*0.147598
    angle = math.radians(30)
    position_in_space=[-5-math.cos(angle)*distance_from_right_side_m,math.sin(angle)*distance_from_right_side_m,height_on_screen_m]
    return(position_in_space)

def get_linear_function_focalpoint1_normal(position_on_screenA):#define function, that goes through the Points, Returns that function with variablename function1
    position_on_screenA_vector=sp.Matrix(position_on_screenA)
    s = sp.symbols('s')
    focalpoint1_vector=sp.Matrix(focal_position1)
    direction_vector1=position_on_screenA_vector-focalpoint1_vector
    function1=position_on_screenA_vector+ s * direction_vector1
    print("FunctionA:", function1)
    return function1, direction_vector1


def get_linear_function_focalpoint2_normal(position_on_screenB):
    position_on_screenB_vector=sp.Matrix(position_on_screenB)
    t = sp.symbols('t')
    focalpoint2_vector=sp.Matrix(focal_position2)
    direction_vector2=position_on_screenB_vector-focalpoint2_vector
    function2=position_on_screenB_vector+ t * direction_vector2
    print("FunctionB:", function2)
    return function2, direction_vector2

st.subheader("1. Blausegmentierung zur Synchronisierung der Videos (Bemerkung: Streamlit ist langsam im Bilder laden, deswegen enpfiehlt es sich das Startframe weiter nach vorne zu setzen")
col1, col2 = st.columns(2)
with col1:
    bild1 = st.empty()
    bild1_segmentiert = st.empty()

with col2:
    bild2 = st.empty()
    bild2_segmentiert = st.empty()

status=st.empty()
#statusblau=st.empty()
cap1 = cv2.VideoCapture(video1)
cap2 = cv2.VideoCapture(video2)

blue_found1=0
blue_found2=0

if not cap1.isOpened():
    print("Video konnte nicht geöffnet werden.")
    exit()

if not cap2.isOpened():
    print("Video konnte nicht geöffnet werden.")
    exit()


    
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    if not ret1:
       print("Video beendet oder Fehler beim Lesen")
       break
    if not ret2:
       print("Video beendet oder Fehler beim Lesen")
       break
    #statusblau.text("Blausegmentierung läuft ...")
        

    if not blue_found1:
        hsv_blue1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask_blue1 = cv2.inRange(hsv_blue1, lower_blue1, upper_blue1)
        coords = cv2.findNonZero(mask_blue1)
        time.sleep(1/30)

        if coords is not None:
            x, y, w, h = cv2.boundingRect(coords)
            bboxblue1 = (x, y, x+w, y+h)
            cv2.rectangle(frame1,(x, y),(x+w, y+h),(255, 0, 0),3)

        else:
            bboxblue1 = None
        print("Blue Bonding Box A:", bboxblue1)
        #bild1.image(frame1, channels="BGR")


        if bboxblue1 is not None:
            frame_number1 = int(cap1.get(cv2.CAP_PROP_POS_FRAMES)) - 1
            blue_found1=True #Diese Variable hindert die Segmentation (ganzer Block) nachdem das erste Mal Blau segmentiert wurde
            print("Blue1 detected!")
            print("Frame1:", frame_number1)
            print("Video:", video_nummer)


    if not blue_found2:
        hsv_blue2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
        mask_blue2 = cv2.inRange(hsv_blue2, lower_blue2, upper_blue2)
        coords = cv2.findNonZero(mask_blue2)
        time.sleep(1/30)

        if coords is not None:
            x, y, w, h = cv2.boundingRect(coords)
            bboxblue2 = (x, y, x+w, y+h)
            cv2.rectangle(frame2,(x, y),(x+w, y+h),(255, 0, 0),3)
            
        else:
            bboxblue2 = None
            
        print("Blue Bonding Box B:", bboxblue2)
        #bild2.image(frame2, channels="BGR")


        if bboxblue2 is not None:
            frame_number2 = int(cap2.get(cv2.CAP_PROP_POS_FRAMES)) - 1
            blue_found2=True
            print("Blue2 detected!")
            print("Frame2:", frame_number2)
            print("Video:", video_nummer)
    
    if blue_found1 and blue_found2:
        cap1.release()
        cap2.release()
        bild1.empty()
        bild2.empty()
        #statusblau.empty()
        break



#2. Teil des Programms->Videos werden vom Frame in dem Blue erkannt wurde abgespielt, hier wird Rot und Grün erkannt
cap1=cv2.VideoCapture(video1)
cap2=cv2.VideoCapture(video2)

if not cap1.isOpened():
    print("Video konnte nicht geöffnet werden.")
    exit()

if not cap2.isOpened():
    print("Video konnte nicht geöffnet werden.")
    exit()

st.subheader("2. Rot-/Grünsegmentierung des 1. Videos Originalbilder mit Boundigbox")

bild1 = st.empty()
bild2 = st.empty()

cap1.set(cv2.CAP_PROP_POS_FRAMES, frame_number1) 

previous_bboxred1=None
previous_bboxred2=None

list_of_functions1_green=[]
list_of_functions1_red=[]
list_of_functions2_green=[]
list_of_functions2_red=[]

frame_count1=start_segmentation

if start_segmentation2 is not None:
    frame_count2=start_segmentation2
else:
    frame_count2=start_segmentation

roired1=None
roired2=None
bboxred1=None
bboxred2=None
bboxgreen1=None
bboxgreen2=None
roigreen1=None
roigreen2=None

masken1_green=[]
masken1_red=[]

gesamt_frames1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
progress1 = st.progress(0)

#1. Video
while True:
    ret1, frame1 = cap1.read()

    if not ret1:
       print("Video beendet oder Fehler beim Lesen")
       break


    roigreen1=frame1[round(pixel_width/2):pixel_width, round(pixel_length/4):pixel_length] #Breite angepasst, wegen Störsegmentation

    hsvgreen1 = cv2.cvtColor(roigreen1, cv2.COLOR_BGR2HSV)


    mask_green1 = cv2.inRange(hsvgreen1, lower_green1, upper_green1)
    print("Erkannte Pixel:", cv2.countNonZero(mask_green1))

    mask_green_full1 = np.zeros(frame1.shape[:2], dtype=np.uint8)
    mask_green_full1[round(pixel_width/2):pixel_width,round(pixel_length/4):pixel_length]=mask_green1


    masken1_green.append(mask_green_full1.copy())

    coords = cv2.findNonZero(mask_green_full1)

    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        bboxgreen1 = (x, y, x+w, y+h)
    else:
        bboxgreen1 = None
          

    if bboxgreen1 is None and previous_bboxred1 is not None:
        print("No green detected in Video A")
        px1red1, py1red1, px2red1, py2red1 = previous_bboxred1

        x1red1 = max(0, px1red1 - 45)
        y1red1 = max(0, py1red1 - 45)
        x2red1 = min(frame1.shape[1], px2red1 + 45)
        y2red1 = min(frame1.shape[0], py2red1 + 45)

        roired1 = frame1[y1red1:y2red1, x1red1:x2red1]
        print("Verwende vorherige RED Boundingbox als ROI")


    elif bboxgreen1 is not None:
        print("Green Boundingbox1:", bboxgreen1)
        position_green1=get_position_in_space1_normal(bboxgreen1)
        print("Green Position in space1:",position_green1)
        if frame_count1>=start_segmentation and frame_count1<=stopp_segmentation:
            function1, direction_vector1=get_linear_function_focalpoint1_normal(position_green1)
            list_of_functions1_green.append((frame_count1,function1,direction_vector1))
        previous_bboxgreen1=bboxgreen1

        x1green1, y1green1, x2green1, y2green1 = bboxgreen1
        cv2.rectangle(frame1,(x1green1, y1green1),(x2green1, y2green1),(0, 255, 0),3)

        x1red1 = max(0, x1green1 - 45)
        y1red1 = max(0, y1green1 - 45)
        x2red1 = min(frame1.shape[1], x2green1 + 45)
        y2red1 = min(frame1.shape[0], y2green1 + 45)

        roired1 = frame1[y1red1:y2red1, x1red1:x2red1]

    else:
        print("Keine Position für ROI vorhanden.")

    if roired1 is not None:

        hsvred1 = cv2.cvtColor(roired1, cv2.COLOR_BGR2HSV)

        submask1_red1 = cv2.inRange(hsvred1, lower_red1_1, upper_red1_1)
        submask2_red1 = cv2.inRange(hsvred1, lower_red2_1, upper_red2_1)

        maskred1 = cv2.bitwise_or(submask1_red1, submask2_red1)

        mask_red_full1 = np.zeros(frame1.shape[:2], dtype=np.uint8)
        mask_red_full1[y1red1:y2red1, x1red1:x2red1] = maskred1

        masken1_red.append(mask_red_full1.copy())
        
        coords = cv2.findNonZero(mask_red_full1)

        if coords is not None:
            x, y, w, h = cv2.boundingRect(coords)
            bboxred1 = (x, y, x+w, y+h)
        else:
            bboxred1 = None

    else:
        bboxred1=None
    
    if bboxred1 is not None:

        rx1, ry1, rx2, ry2 = bboxred1
        
        cv2.rectangle(frame1,(rx1, ry1),(rx2, ry2),(0, 0, 255),3)

        previous_bboxred1 = (rx1,ry1,rx2,ry2)

        print("Red Boundingbox1 adapted:", previous_bboxred1)
        position_red1=get_position_in_space1_normal(previous_bboxred1)
        print("Red Position in space 2:", position_red1)
        if frame_count1>=start_segmentation and frame_count1<=stopp_segmentation:
            function1, direction_vector1=get_linear_function_focalpoint1_normal(position_red1)
            list_of_functions1_red.append((frame_count1,function1, direction_vector1))

    else:

        print("No red detected in Video A")
   
    frame_count1+=1
    print("Aktueller Frame:", frame_count1)
    print("Anzahl gespeicherter Masken:", len(masken1_red))

    if gesamt_frames1 > 0:
        fortschritt1 = min(frame_count1 / gesamt_frames1, 1.0)
        progress1.progress(fortschritt1)    


    #if frame_count1 % 2 == 0:
        #bild1.image(frame1, channels="BGR")

    status.text("Video A wird analysiert ...")

    
    time.sleep(1/25)
    if frame_count1>landing_red:
        break


cap1.release()
bild1.empty()
status.empty()
progress1.progress(1.0)

st.subheader("Segmentierte Maske")

bild_maske = st.empty()
#progress_wiedergabe=st.progress(0,text="Anzeige Maske")

for i, maske_green in enumerate(masken1_green):
    for i, maske_red in enumerate(masken1_red):

        colored1 = np.zeros_like(frame1)

        colored1[maske_red > 0] = [0, 0, 255]

        colored1[maske_green > 0] = [0, 255, 0]
        
        #bild_maske.image(colored1, clamp=True)

        #progress_wiedergabe.progress((i + 1) / len(masken1_green))

        time.sleep(1 / 30)
#progress_wiedergabe.progress(1.0)
        


st.subheader("3. Rot-/Grünsegmentierung des 2. Videos Originalbilder mit Boundigbox")

masken2_green=[]
masken2_red=[]

gesamt_frames2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
progress2 = st.progress(0)

#if start_segmentation2 is not None:
    #cap2.set(cv2.CAP_PROP_POS_FRAMES, frame_number2+start_segmentation2)
#else:
    #cap2.set(cv2.CAP_PROP_POS_FRAMES, frame_number2+start_segmentation)

cap2.set(cv2.CAP_PROP_POS_FRAMES, frame_number2)



#2. Video
while True:
    ret2, frame2 = cap2.read()
    if not ret2 or frame2 is None:
       print("Video beendet oder Fehler beim Lesen")
       break

    roigreen2=frame2[round((2/3)*pixel_width):pixel_width, 0:round((4/5)*pixel_length)]#Region of interest angepasst wegen grüner Bande:)
    hsvgreen2 = cv2.cvtColor(roigreen2, cv2.COLOR_BGR2HSV)

    mask_green2 = cv2.inRange(hsvgreen2, lower_green2, upper_green2)

    mask_green_full2 = np.zeros(frame2.shape[:2], dtype=np.uint8)
    mask_green_full2[round((2/3)*pixel_width):pixel_width,0:round((4/5)*pixel_length)]=mask_green2

    masken2_green.append(mask_green_full2.copy())

    coords = cv2.findNonZero(mask_green_full2)

    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        bboxgreen2 = (x, y, x+w, y+h)
    else:
        bboxgreen2 = None


    if bboxgreen2 is None and previous_bboxred2 is not None:
        print("No green detected in Video B")
        px1red2, py1red2, px2red2, py2red2 = previous_bboxred2

        x1red2 = max(0, px1red2 - 45)
        y1red2 = max(0, py1red2 - 45)
        x2red2 = min(frame2.shape[1], px2red2 + 45)
        y2red2 = min(frame2.shape[0], py2red2 + 45)

        roired2 = frame2[y1red2:y2red2, x1red2:x2red2]
        print("Verwende vorherige RED Boundingbox als ROI")


    elif bboxgreen2 is not None:
        print("Green Boundingbox2:", bboxgreen2)
        position_green2=get_position_in_space2_normal(bboxgreen2)
        print("Green Position in Space Video2:", position_green2)
        if start_segmentation2 is not None:
            if frame_count2>=start_segmentation2 and frame_count2<=stopp_segmentation2:
                function2, direction_vector2=get_linear_function_focalpoint2_normal(position_green2)
                list_of_functions2_green.append((frame_count2,function2,direction_vector2))
        else:
            if frame_count2>=start_segmentation and frame_count2<=stopp_segmentation:
                function2, direction_vector2=get_linear_function_focalpoint2_normal(position_green2)
                list_of_functions2_green.append((frame_count2,function2,direction_vector2))
        previous_bboxgreen2=bboxgreen2
        

        x1green2, y1green2, x2green2, y2green2 = bboxgreen2
        cv2.rectangle(frame2,(x1green2, y1green2),(x2green2, y2green2),(0, 255, 0),3)

        x1red2 = max(0, x1green2 - 45)
        y1red2 = max(0, y1green2 - 45)
        x2red2 = min(frame2.shape[1], x2green2 + 45)
        y2red2 = min(frame2.shape[0], y2green2 + 45)

        roired2 = frame2[y1red2:y2red2, x1red2:x2red2]


    else:
        print("Keine Position für ROI vorhanden.")

    if roired2 is not None:

        hsvred2 = cv2.cvtColor(roired2, cv2.COLOR_BGR2HSV)

        submask1_red2 = cv2.inRange(hsvred2, lower_red1_2, upper_red1_2)
        submask2_red2 = cv2.inRange(hsvred2, lower_red2_2, upper_red2_2)

        maskred2 = cv2.bitwise_or(submask1_red2, submask2_red2)

        mask_red_full2 = np.zeros(frame2.shape[:2], dtype=np.uint8)
        mask_red_full2[y1red2:y2red2, x1red2:x2red2] = maskred2

        masken2_red.append(mask_red_full2.copy())

        coords = cv2.findNonZero(mask_red_full2)

        if coords is not None:
            x, y, w, h = cv2.boundingRect(coords)
            bboxred2 = (x, y, x+w, y+h)
        else:
            bboxred2 = None

    else:
        bboxred2=None

    if bboxred2 is not None:

        r2x1, r2y1, r2x2, r2y2 = bboxred2

        cv2.rectangle(frame2,(r2x1, r2y1),(r2x2, r2y2),(0, 0, 255),3)

        previous_bboxred2 = (r2x1,r2y1,r2x2,r2y2)

        print("Red Boundingbox2 adapted:", previous_bboxred2)
        position_red2=get_position_in_space2_normal(previous_bboxred2)
        print("Red Position in Space 2:",position_red2)
        if start_segmentation2 is not None: 
            if frame_count2>=start_segmentation2 and frame_count2<=stopp_segmentation2:
                function2, direction_vector2=get_linear_function_focalpoint2_normal(position_red2)
                list_of_functions2_red.append((frame_count2,function2, direction_vector2))
        else:
            if frame_count2>=start_segmentation and frame_count2<=stopp_segmentation:
                function2, direction_vector2=get_linear_function_focalpoint2_normal(position_red2)
                list_of_functions2_red.append((frame_count2,function2,direction_vector2))
        
    else:

        print("No red detected in Video B")
    
   
    frame_count2+=1
    print("Aktueller Frame:", frame_count2)
    print("Anzahl gespeicherter Masken:", len(masken2_red))

    if gesamt_frames2 > 0:
        fortschritt2 = min(frame_count2 / gesamt_frames2, 1.0)
        progress2.progress(fortschritt2)   


    #if frame_count2 % 2 == 0:
        #bild2.image(frame2, channels="BGR")
    
    status.text("Video B wird analysiert ...")
    
    time.sleep(1/25)

    if stopp_segmentation2 is not None:
        if frame_count2>stopp_segmentation2:
            break
    else:
        if frame_count2>stopp_segmentation:
            break

cap2.release()
progress1.progress(1.0)

bild2.empty()
status.empty()

st.subheader("Segmentierte Maske")
#progress_wiedergabe=st.progress(0,text="Anzeige Maske")
for i, maske_green in enumerate(masken2_green):
    for i, maske_red in enumerate(masken2_red):

        colored2 = np.zeros_like(frame2)

        colored2[maske_red > 0] = [0, 0, 255]

        colored2[maske_green > 0] = [0, 255, 0]
        
        #bild_maske.image(colored2, clamp=True)

        #progress_wiedergabe.progress((i + 1) / len(masken2_green))
        time.sleep(1/30)
#progress_wiedergabe.progress(1.0)

st.write("List of green functions 1:", list_of_functions1_green)
st.write("List of red functions 1:", list_of_functions1_red)

st.write("List of green functions 2:", list_of_functions2_green)
st.write("List of red functions 2:", list_of_functions2_red)


s = sp.symbols('s')
t = sp.symbols('t')
position_greenpoint=[]
position_redpoint=[]

if video_nummer in (4,7,10,13,15):
    for frame1, function1, direction1 in list_of_functions1_green:
        for frame2, function2, direction2 in list_of_functions2_green:

            if frame1 == frame2:

                difference_functions=function1-function2 #Differenz der Funktionen
                eqn1=difference_functions.dot(direction1)#Gleichungssystem aufstellen
                eqn2=difference_functions.dot(direction2)
                solution=sp.solve([eqn1,eqn2],[s,t]) #Gleichungssystem lösen
                if solution:
                    s_value = solution[s]
                    t_value = solution[t]

                    point1 = function1.subs(s, s_value)
                    point2 = function2.subs(t, t_value)

                    mean_point = (point1 + point2) / 2

                    position_greenpoint.append([list(mean_point),frame1])

    print("Green Point at certain frame:",position_greenpoint)
    st.subheader("3D-Position Grünepunkte:")
    st.write(position_greenpoint)

    #Position für Rot
    for frame1, function1, direction1 in list_of_functions1_red:
        for frame2, function2, direction2 in list_of_functions2_red:

            if frame1 == frame2:
                difference_functions=function1-function2
                eqn1=difference_functions.dot(direction1)
                eqn2=difference_functions.dot(direction2)
                solution=sp.solve([eqn1,eqn2],[s,t])
                if solution:
                    s_value = solution[s]
                    t_value = solution[t]

                    point1 = function1.subs(s, s_value)
                    point2 = function2.subs(t, t_value)

                    mean_point = (point1 + point2) / 2

                    position_redpoint.append([list(mean_point),frame1])


    print("Red Point at certain frame:",position_redpoint)
    st.subheader("3D-Position Rotepunkte:")
    st.write(position_redpoint)

if video_nummer in (5,6,8,11,16,17):
    factor=1.877
if video_nummer in (9,12,14):
    factor=1.92
if video_nummer==9:
    factor=1.9

if video_nummer in (5,6,8,9,11,12,14,16,17):
    for frame1, function1, direction1 in list_of_functions1_green:
        for frame2, function2, direction2 in list_of_functions2_green:

            if frame1 == frame2/factor:

                difference_functions=function1-function2 #Differenz der Funktionen
                eqn1=difference_functions.dot(direction1)#Gleichungssystem aufstellen
                eqn2=difference_functions.dot(direction2)
                solution=sp.solve([eqn1,eqn2],[s,t]) #Gleichungssystem lösen
                if solution:
                    s_value = solution[s]
                    t_value = solution[t]

                    point1 = function1.subs(s, s_value)
                    point2 = function2.subs(t, t_value)

                    mean_point = (point1 + point2) / 2

                    position_greenpoint.append([list(mean_point),frame1])

    print("Green Point at certain frame:",position_greenpoint)
    st.subheader("3D-Position Grünepunkte:")
    st.write(position_greenpoint)

    #Position für Rot
    for frame1, function1, direction1 in list_of_functions1_red:
        for frame2, function2, direction2 in list_of_functions2_red:

            if frame1 == frame2/factor:
                difference_functions=function1-function2
                eqn1=difference_functions.dot(direction1)
                eqn2=difference_functions.dot(direction2)
                solution=sp.solve([eqn1,eqn2],[s,t])
                if solution:
                    s_value = solution[s]
                    t_value = solution[t]

                    point1 = function1.subs(s, s_value)
                    point2 = function2.subs(t, t_value)

                    mean_point = (point1 + point2) / 2

                    position_redpoint.append([list(mean_point),frame1])


    print("Red Point at certain frame:",position_redpoint)
    st.subheader("3D-Position Rotepunkte:")
    st.write(position_redpoint)
#Test Framepaare Slowmotion

#frames_green1 = {frame for frame, function, direction in list_of_functions1_green}

#frames_green2 = {frame for frame, function, direction in list_of_functions2_green}

#print("Anzahl grüne Sichtlinien A:", len(frames_green1))
#print("Anzahl grüne Sichtlinien B:", len(frames_green2))

#matching_frames = [(frame1, frame2) for frame1 in sorted(frames_green1) for frame2 in sorted(frames_green2) if frame1 == frame2 / 2]

#print("Passende Frame-Paare:", matching_frames[:20])
#print("Anzahl passender Paare:", len(matching_frames))


#Funktion durch Roter und Grüner Punkt auf xy-Ebene projiziert (nur Richtungsvektor)

list_redgreen=[]
for position_red, frame1 in position_redpoint:
    for position_green, frame2 in position_greenpoint:
        if frame1==frame2:
            function_redgreen=sp.Matrix([position_green[0]-position_red[0],position_green[1]-position_red[1]])
            function_redgreen_projected=function_redgreen[:2,:]
            list_redgreen.append((function_redgreen_projected,frame1))
print("List Red to Green Points:", list_redgreen)
st.subheader("Fuktionen durch Rote und Grüne Punkte:")
st.write(list_redgreen)
 

#Konstanten zuerst auf None setzten
#mean_take_off=None
#mean_landing=None
mean_landing_position=[]
mean_take_off_position=[]
total_angle=0
angle_old=None
list_angles=[]
old_height_green=None
old_height_red=None


#Absprungframes 3 Fälle unterschieden
if take_off_red is not None and take_off_green is not None:
    mean_take_off=(take_off_red+take_off_green)/2
    print("Mean Take Off:", mean_take_off)

elif take_off_red is not None and take_off_green is None:
    mean_take_off=take_off_red
    print("Mean Take Off:", mean_take_off)

elif take_off_green is not None and take_off_red is None:
    mean_take_off=take_off_green
    print("Mean Take Off:", mean_take_off)

mean_landing=(landing_green+landing_red)/2

take_off_red_position, take_off_red = min(position_redpoint,key=lambda eintrag: abs(eintrag[1] - mean_take_off))

landing_position_red, landing_red = min(position_redpoint,key=lambda eintrag: abs(eintrag[1] - mean_landing))

take_off_green_position, take_off_green = min(position_greenpoint,key=lambda eintrag: abs(eintrag[1] - mean_take_off))

landing_position_green, landing_green = min(position_greenpoint,key=lambda eintrag: abs(eintrag[1] - mean_landing))

if video_nummer in (4,7,8,10,11,12,13,14,15,16):

#Absprungort in 3 Fällen unterschieden
    if  take_off_red_position is not None and take_off_green_position is not None:
        xdir=(take_off_green_position[0]+take_off_red_position[0])/2
        ydir=(take_off_green_position[1]+take_off_red_position[1])/2
        mean_take_off_position.append(xdir)
        mean_take_off_position.append(ydir)
        print("Mean Take Off Position:", mean_take_off_position)

    elif take_off_red_position is not None and take_off_green_position is None:
        mean_take_off_position=take_off_red_position
        print("Mean Take Off Position:", mean_take_off_position)

    elif take_off_green_position is not None and take_off_red_position is None:
        mean_take_off_position=take_off_green_position
        print("Mean Take Off Position:", mean_take_off_position)



#Landungsort in 3 verschiedenen Fällen->mean_landing_position enthält x-Position dann y-Position
    if len(landing_position_red)!=0 and len(landing_position_green)!=0:
        mean_xdir=(landing_position_green[0]+landing_position_red[0])/2
        mean_ydir=(landing_position_green[1]+landing_position_red[1])/2
        mean_landing_position.append(mean_xdir)
        mean_landing_position.append(mean_ydir)
        print("Mean Landing Place on xy-Plane:", mean_landing_position)

    elif len(landing_position_red)!=0 and len(landing_position_green)==0:
        mean_xdir=landing_position_red[0]
        mean_ydir=landing_position_red[1]
        mean_landing_position.append(mean_xdir)
        mean_landing_position.append(mean_ydir)
        print("Mean Landing Place on xy-Plane:", mean_landing_position)

    elif len(landing_position_green)!=0 and len(landing_position_red)==0:
        mean_xdir=landing_position_green[0]
        mean_ydir=landing_position_green[1]
        mean_landing_position.append(mean_xdir)
        mean_landing_position.append(mean_ydir)
        print("Mean Landing Place on xy-Plane:", mean_landing_position)

    if mean_take_off is not None and mean_landing is not None:
        airtime=(mean_landing-mean_take_off)/30 #durch FPS teilen
        print("Time in the air:", airtime)

st.subheader("Absprung-/ und Landekoordinaten:")
print("Absprungframe", mean_take_off)
st.write("Absprungframe", mean_take_off)
print("Absprungposition", mean_take_off_position)
st.write("Absprungposition", mean_take_off_position)
print("Landungsframe", mean_landing)
st.write("Landungsframe", mean_landing)
print("Landungsposition", mean_landing_position)
st.write("Landungsposition", mean_landing_position)


#Winkeländerungsfunktion
def winkel_aenderung(v1, v2):
    v1 = sp.Matrix(v1)
    v2 = sp.Matrix(v2)

    dotp = (v1.T * v2)[0]
    crossp = v1[0] * v2[1] - v1[1] * v2[0]

    winkel = sp.atan2(crossp, dotp) * 180 / sp.pi

    winkel=float(winkel.evalf())

    if winkel < 0:
        winkel += 360

    return winkel


#Richtung des Sprungs berechnen

list_delta_angles = []#Gibt Winkeldifferenz zum vorherigen Datenpunkt an
rotation_velocity=[]
sum_angle=0.0
total_angle=0.0
total_rotation=[]
list_rotation = [] # Gibt Winkeldifferenz gesammt zum Frame an (aufsummiert von Beginn bis zu jedem Datenpunkt)
list_rotation_corrected=[]
sum_angle=0
count_angle=0
avg_total_angle=0



if len(mean_landing_position)!=0:
    jumpdirection=sp.Matrix([float(mean_take_off_position[0]-mean_landing_position[0]),float(mean_take_off_position[1]-mean_landing_position[1])])
    previous_position = None
    for position, frame in list_redgreen:
        if frame>mean_take_off and frame<mean_landing:
            position = sp.Matrix(position)
        
            if previous_position is not None:
                delta_angle = winkel_aenderung(previous_position,position)
                list_delta_angles.append((delta_angle, frame))

                sum_angle += delta_angle

                list_rotation.append((sum_angle, frame))

            previous_position = position

    print("Kumulative Rotation:", list_rotation)
    print("Winkeldifferenz von Datenpunkt zu Datenpunkt:", list_delta_angles)


    take_off_time=mean_take_off/30
    landing_time=mean_landing/30
    jump_time=landing_time-take_off_time
    jump_frames=mean_landing-mean_take_off

    for angle, frame in list_rotation:
        midpoint_jump=jump_frames/2    #Prüft, ob der Messpunkt schon bei der zweiten Rotation stattgefunden hat
        frame=frame-mean_take_off

        if frame>=midpoint_jump:
            angle+=360

        frame=frame+mean_take_off
        list_rotation_corrected.append((angle, frame))
    print("Liste von Rotationsmesspunkten mit Falluntescheidung (+360° in der zweiten Rotation):", list_rotation_corrected)

    if jump_time>0:
    
        for angle, frame in list_rotation_corrected:

            current_time=frame/30

            delta_time=current_time-take_off_time

            if delta_time>0:

                angular_velocity=angle/delta_time
                total_angle=angular_velocity*(jump_time)
                if video_nummer in (4,5,6):
                    total_angle-=180
                rotation_velocity.append((angular_velocity,frame))#Liste mit Winkelgeschwindigkeit und frame, mit welchem sie berechnet wurde
                total_rotation.append((total_angle, frame))


            else:
                print("Sprungdauer muss positiv sein.")

        if len(total_rotation)!=0:
            for angle, frame in total_rotation: 
                sum_angle+=angle
                count_angle+=1
            avg_tot_angle=sum_angle/count_angle
        if avg_total_angle!=0:

            print("Gesamtrotation des Sprungs(Durchschnitt aller Messpunkte:", avg_total_angle)
            
        print("Gesamtrotation des Sprungs(Annahme konstante Rotationsgeschwindigkeit):", total_rotation)

        print("Winkelgeschwindigkeit mit zugehörigem frame:", rotation_velocity)


#Weite berechnen
if mean_take_off_position is not None and len(mean_landing_position)!=0:
    jump_distance=sp.sqrt((mean_landing_position[0]-mean_take_off_position[0])**2+(mean_landing_position[1]-mean_take_off_position[1])**2)
    print("Jumpdistance:", jump_distance)



#Höhe berechnen
for position1, frame1 in position_greenpoint:
    current_height=position1[2]
    if old_height_green is None or current_height>old_height_green:
         old_height_green=current_height

for position2, frame2 in position_redpoint:
    current_height=position2[2]
    if old_height_red is None or current_height>old_height_red:
         old_height_red=current_height

if take_off_plane_red is not None and take_off_plane_green is not None:
    if old_height_green is not None and old_height_red is not None:
        abs_height_green=old_height_green-take_off_plane_green
        abs_height_red=old_height_red-take_off_plane_red
        max_height = (abs_height_green + abs_height_red) / 2
        difference_abs_heights=abs_height_green-abs_height_red
        percent_of_max_height=(difference_abs_heights/max_height)*100
        print("Maxheight (in m):", max_height)
        print("Difference of Green and Red maximum heights:", difference_abs_heights)
        print("Percentage Difference of the Maximum height:", percent_of_max_height)

elif take_off_plane_red is None and take_off_plane_green is not None:
    if old_height_green is not None:
        max_height=old_height_green-take_off_plane_green
        print("Maxheight (in m, only used green):", max_height)

elif take_off_plane_green is None and take_off_plane_red is not None:
    if old_height_red is not None:
        max_height=old_height_red-take_off_plane_red
        print("Maxheight (in m, only used red):", max_height)

else:
    print("Es wurden nicht für beide Punkte Höhen gefunden.")


print("Landingplane green:", landingplane_green)
print("Landingplane red:", landingplane_red)



position_redpoint_seg=[]
position_greenpoint_seg=[]

#Einschränken der Daten auf Absprung bis Landung
for position, frame in position_redpoint:
    if frame>start_segmentation and frame<stopp_segmentation:
        position_redpoint_seg.append([position, frame])

for position, frame in position_greenpoint:
    if frame>start_segmentation and frame<stopp_segmentation:
        position_greenpoint_seg.append([position, frame])


#CSV-Datei erstellen:
#with open("Video 4 Ergebnisse.csv", "w", newline="", encoding="utf-8-sig") as datei:
    #writer = csv.writer(datei, delimiter=";")

    #writer.writerow(["Take-off Frame", "Take-off Position", "Landungs Frame", "Landungs Position", "Sprungrichtung", "Luftzeit", "Max. Höhe", "Weite","Rotation"])

    #writer.writerow([mean_take_off, mean_take_off_position, mean_landing, mean_landing_position, jumpdirection, airtime, max_height, jump_distance, avg_total_angle])



#with open("Video 4 Koordinaten.csv", "w", newline="", encoding="utf-8-sig") as datei:
    #writer = csv.writer(datei, delimiter=";")

    #writer.writerow(["Farbe","Frame", "X", "Y", "Z"])

    #for position, frame in position_redpoint_seg:
        #writer.writerow(["Red", frame, position[0], position[1], position[2]])

    #writer.writerow(["Farbe","Frame", "X", "Y", "Z"])

    #for position, frame in position_greenpoint_seg:
        #writer.writerow(["Green", frame, position[0], position[1], position[2]])



#Punkte in einem Koordinatensystem plotten
#green_points = np.array([position for position, frame in position_greenpoint_seg], dtype=float)

#red_points = np.array([position for position, frame in position_redpoint_seg], dtype=float)

#if take_off_plane_green is not None:
    #green_points[:, 2] -= take_off_plane_green

#elif landingplane_green is not None:
    #green_points[:, 2] -= landingplane_green

#if take_off_plane_red is not None:
    #red_points[:, 2] -= take_off_plane_red

#elif landingplane_red is not None:
    #red_points[:, 2] -= landingplane_red

#green_cloud = pv.PolyData(green_points)
#red_cloud = pv.PolyData(red_points)

# Kugel-Geometrie definieren
#sphere = pv.Sphere(radius=0.02,phi_resolution=16,theta_resolution=16)

# Für jeden Punkt eine Kugel erzeugen
#green_spheres = green_cloud.glyph(geom=sphere,scale=False)

#red_spheres = red_cloud.glyph(geom=sphere,scale=False)

# Darstellung
#plotter = pv.Plotter()

#plotter.add_mesh(green_spheres,color="green",smooth_shading=True,label="Grüne Punkte")

#plotter.add_mesh(red_spheres,color="red",smooth_shading=True,label="Rote Punkte")

#plotter.add_axes()
#plotter.show_grid()
#plotter.add_legend()
#plotter.show()

#green_cloud = pv.PolyData(green_points)
#red_cloud = pv.PolyData(red_points)

#plotter = pv.Plotter()

#plotter.add_points(green_cloud,color="green",point_size=8,render_points_as_spheres=True,label="Green points")

#plotter.add_points(red_cloud,color="red",point_size=8,render_points_as_spheres=True,label="Red points")





