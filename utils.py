import cv2

def orb_sim(img1, img2):
    orb = cv2.ORB_create()
    kpa, descr_a = orb.detectAndCompute(img1, None)
    kpb, descr_b = orb.detectAndCompute(img2, None)

    comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = comp.match(descr_a, descr_b)
    regiones_similares = [i for i in matches if i.distance < 70]

    if len(matches) == 0:
        return 0
    return len(regiones_similares) / len(matches)
