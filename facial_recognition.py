import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from utils import orb_sim

def login_facial(verificacion_usuario):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Login Facial', frame)
        if cv2.waitKey(1) == 27:  # Presiona ESC para salir
            break
    cv2.imwrite(f"images/{verificacion_usuario.get()}_LOG.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()

    img = f"images/{verificacion_usuario.get()}_LOG.jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)

    # Aquí deberías implementar la comparación de rostros usando `orb_sim`
